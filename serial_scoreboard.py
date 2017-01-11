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

def main(teamname):
	mb_port = get_microbit_port()
	if mb_port is None:
		raise RuntimeError("Could not find micro:bit comport!")
	print(mb_port)

	r = requests.get(LEADERBOARD_URL % ("c", teamname))
	if r.status_code != 200:
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
					raise RuntimeError("NON-200: %s" % (r.status_code,))

			elif typ == "over":
				print("OVER")
				break

if __name__ == "__main__":
	while True:
		i = random.randint(0, 9999999)
		print("NEW TEAM %d" % (i,))
		main("team %d" % (i,))
