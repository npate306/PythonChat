import socket
import tkinter as tk
def messages(socket):
    while True:
        message = input("Enter here: ")
        socket.send(message.encode())
        print(socket.recv(1024).decode())
server = socket.socket()
print ("Socket successfully created")
port = 12345
server.bind(("127.18.1.1", port))
print ("socket binded to %s" % (port))
server.listen(5)
print ("socket is listening")
while True:
    c, address = server.accept()
    messages(c)