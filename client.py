import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.56.1" #computer as the server
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket setup
client.connect(ADDR) #connecting client and the server

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT) #encode in utf8
    send_length += b' ' * (HEADER - len(send_length)) #to make the msg the correct length. we use 64bytes
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
input()
send("Hello World, Second Message!")
input()
send("Hello World, Third Message!")

send(DISCONNECT_MESSAGE)