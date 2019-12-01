#!/usr/bin/python3          # This is client.py file

import socket               # Import socket module
import threading
import time

# creates socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
flag = True
port = 5456

while(flag):
    # time.sleep(1)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.1.25", port))
        time.sleep(1)
        tm = s.recv(1024) # msg can only be 1024 bytes long
        s.close()
        time.sleep(1)
        print("Status: %s" % tm.decode('ascii'))
    except Exception as e:
        print(e)
        flag = False
        pass
        

if(not flag):
    {
        print("Server is out")
    }


# def checkIfAlive():
    

# t1 = threading.Thread(target=checkIfAlive)

