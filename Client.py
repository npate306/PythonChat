import socket
def messages(socket):
    while True:
        print(socket.recv(1024).decode())
        message = input("Enter here: ")
        socket.send(message.encode())
s = socket.socket()
port = 12345
sendMessageThreads = []
receiveMessageThreads = []
s.connect(("127.18.1.1", port))
while True:
    messages(s)
s.close()