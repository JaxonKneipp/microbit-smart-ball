import network
import utime
import socket

sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('Jamies Phone', '1win72d6bsuq')

while not sta_if.isconnected():
	utime.sleep(0.1)
	
# http://ncss.seansweb.com.au/main.php?action=i&gamename=YAY!!
addr_info = socket.getaddrinfo('ncss.seansweb.com.au', 80)

addr = addr_info[0][-1]
	
s = socket.socket()
s.connect(addr)

s.send(b'GET /main.php?action=i&gamename=foo HTTP/1.1\r\nHost: ncss.seansweb.com.au\r\n\r\n')

while True:
	data = s.recv(500)
	print(data.decode(),end='')
	