import socket               # Import socket module
import time
import os
import smtplib

# creates socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.settimeout(5)

flag = True

port = 5456

EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

def notifyUser():
    subject = 'YOUR SITE IS DOWN!'
    body = 'Make sure the server restarted and it is back up'
    msg = f'Subject: {subject}\n\n{body}'
    # temp = msg.as_string()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
    server.quit()
    # smtp.sendmail(EMAIL_ADDRESS, 'EMAIL_ADDRESS', temp)

while(flag):
    # time.sleep(1)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("192.168.1.25", port))
        time.sleep(1)
        tm = s.recv(1024) # msg can only be 1024 bytes long
        s.close()
        time.sleep(300)
        # print("Status: %s" % tm.decode('ascii'))
    except Exception as e:
        print(e)
        flag = False
        pass
        
notifyUser()