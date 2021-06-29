import socket 
import threading

HEADER = 64#64bytes
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname()) #togetipadressofthecomputer
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"#revice this message, disconnect  immedeiately
#print(SERVER) this line will print 192.168.56.1 (my computer's ip)(can be different when running on diff computer)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#made socket with typ of socket AF_INET
server.bind(ADDR)#bind server with ADDR

def handle_client(conn, addr):#connection and address Handles connection between client and server
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)#program not pass this line until we recieve message from client. DEcode using utf8
        if msg_length:
            msg_length = int(msg_length)#tells us length of msg
            msg = conn.recv(msg_length).decode(FORMAT)#decode using utf8
            if msg == DISCONNECT_MESSAGE:#to end connection if DISCONNECT_MESSAGE is recieved
                connected = False

            print(f"[{addr}] {msg}")#print the address and the msg
            conn.send("Msg received".encode(FORMAT))

    conn.close()
        

def start(): #start socket server
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")#will print the computer's ip address
    while True:#listen to server until sometingbad happened
        conn, addr = server.accept()#wait for new connection n store address, store actual objt to allow to send info back to connection
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()#starting a new thread
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")#print the number of active threads. -1 because start thread always running


print("[STARTING] server is starting...")
start()

