#!/usr/bin/python3
import socket
import time


# creating a socket object
s = socket.socket()
port = 5456
'''
#The reason you are seeing the behaviour you are is that the OS is reserving that particular port for some time after the last connection terminated. 
#This is so that it can properly discard any stray further packets that might come in after the application has terminated.
#By setting the SO_REUSEADDR socket option, you are telling the OS that you know what you're doing and you still want to bind to the same port.
'''
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# bind to pot
s.bind(("192.168.1.25", port))

# Que up to 5 requests
s.listen(5)
bytes2Send = str.encode("All Ok")
while True:
    # establish connection
    (clientSocket, addr) = s.accept()
#    currentTime = time.ctime(time.time()) + "\r\n"
#   clientSocket.send(currentTime.encode('ascii'))
    clientSocket.sendall(bytes2Send)
    clientSocket.close()
