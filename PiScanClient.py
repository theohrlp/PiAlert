#!/usr/bin/python3          # This is client.py file

import socket               # Import socket module

REMOTE_SERVER = "RasBoy.myddns.rocks"
import socket
# creates socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostbyname(REMOTE_SERVER) # or just use (host = '')
port = 5456

s.connect(("192.168.1.25", port))

tm = s.recv(1024) # msg can only be 1024 bytes long

s.close()
print("Status %s" % tm.decode('ascii'))