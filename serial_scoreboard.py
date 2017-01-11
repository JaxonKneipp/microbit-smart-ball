#!/usr/bin/env python3
# Copyright (c) 2017 Aleksa Sarai
# Copyright (c) 2017 Alice Cao
# Copyright (c) 2017 Jaxon Kneipp
# Copyright (c) 2017 Kim Armstrong
# Copyright (c) 2017 Sean Hall
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import random

import tkinter as tk
import requests
import serial
import serial.tools.list_ports

MICROBIT_DESCRIPTOR = "mbed"
MICROBIT_BAUDRATE = 115200

LEADERBOARD_URL = "http://ncss.seansweb.com.au/main.php?action=%s&gamename=%s"

def get_microbit_port():
	for com in serial.tools.list_ports.comports():
		name, desc, _ = com
		if MICROBIT_DESCRIPTOR in desc:
			return name
	return None

class Application(tk.Frame):
	def __init__(self, master=None):

		super().__init__(master)
		self.master = master
		self.pack()
		self.master.geometry("1000x500")
		self.create_widgets()

	def create_widgets(self):

		self.smartSoccerLabel = tk.Label(self, text="Smart ball", font=("Monospace", 25), pady=10)
		self.smartSoccerLabel.pack()

		self.attributionLabel = tk.Label(self, text="by Jaxon Kneipp, Sean Hall, Kim Armstrong and Alice Cao", font=("Monospace", 10))
		self.attributionLabel.pack()

		self.welcomeLabel = tk.Label(self, text="Welcome, Please enter the name of your team.", font=("Monospace", 12))
		self.welcomeLabel.pack()

		self.teamName = tk.StringVar()

		self.teamNameEntry = tk.Entry(self, textvariable=self.teamName)
		# self.teamNameEntry.bind("<Enter>", self.submit_text)
		self.teamNameEntry.pack()

		self.button = tk.Button(self, text="OK", command=self.submit_text)
		self.button.pack()

	def submit_text(self, *_):
		teamname = self.teamName.get()
		if not teamname:
			return

		self.teamName.set("")
		self.button['state'] = tk.DISABLED

		mb_port = get_microbit_port()
		if mb_port is None:
			self.button['state'] = tk.NORMAL
			raise RuntimeError("Could not find micro:bit comport!")
		print(mb_port)

		r = requests.get(LEADERBOARD_URL % ("c", teamname))
		if r.status_code != 200:
			self.button['state'] = tk.NORMAL
			raise RuntimeError("NON-200: %s" % (r.status_code,))

		with serial.Serial(port=mb_port, baudrate=MICROBIT_BAUDRATE) as ser:
			while True:
				line = ser.readline().decode("latin1")
				line = line.strip()

				print("GOT: %s" % line)

				typ, *args = line.split()

				if typ == "count":
					counter = int(args[0])
					print("TEAM: %d" % (counter,))

					r = requests.get(LEADERBOARD_URL % ("i", teamname))
					if r.status_code != 200:
						self.button['state'] = tk.NORMAL
						raise RuntimeError("NON-200: %s" % (r.status_code,))

				elif typ == "over":
					print("OVER")
					self.button['state'] = tk.NORMAL
					break

if __name__ == "__main__":
	root = tk.Tk()
	app = Application(master=root)
	app.mainloop()
