#!/usr/bin/python3          # This is client.py file

import socket               # Import socket module
import time
import os
import smtplib

# creates socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

flag = True

port = 5456

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def notifyUser():
    print("Hello")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("theotriton@gmail.com", "eimaimiarozarkoudapouxorebei12")
    server.sendmail("theotriton@gmail.com", "theotriton@gmail.com", "this message is from python")
    server.quit()
    # with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        # smtp.ehlo()
        # smtp.starttls()
        # smtp.ehlo()
    # smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    # subject = 'YOUR SITE IS DOWN!'
    # body = 'Make sure the server restarted and it is back up'
    # msg = f'Subject: {subject}\n\n{body}'
    # temp = msg.as_string()
    # smtp.sendmail(EMAIL_ADDRESS, 'EMAIL_ADDRESS', temp)
    print("Hello")

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
        
notifyUser()



