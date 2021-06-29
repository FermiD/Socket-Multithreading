# Socket-Multithreading

To start, change SERVER in client.py into the desired ip because for the current SERVER value, I am using my computer's ip. To use your computer, ip, go to command prompt, type ipconfig. Or just run socket.gethostbyname(socket.gethostname()) to get the ip.
Run the server.py to start the server, make sure its running. Then open command prompt, open the project directory where you store client.py. Type python client.py to run the client.py from commandprompt.
A message will be shown:
[STARTING] server is starting...
[LISTENING] Server is listening on 192.168.56.1
[NEW CONNECTION] ('192.168.56.1', 58994) connected.
[ACTIVE CONNECTIONS] 1

This means the connection was established.

To send the messages, run client.py. In client.py, you can see these lines: 
send("Hello World!")
input()
send("Hello World Second Message!")
input()
send("Hello World Third Message!")

send(DISCONNECT_MESSAGE)

THose lines are the messages. You can delete or change the however you want. But, everytime you send a wrote a message, you will have to run client.py again. So haveing three messages needs you to run client.py three times.
The result of sending the message will be shown in the server.py terminal like this:
[('192.168.56.1', 58994)] Hello World!
[('192.168.56.1', 58994)] Hello World Second Message!
[('192.168.56.1', 58994)] Hello World Third Message!
[('192.168.56.1', 58994)] !DISCONNECT

The last line disconnects the client from the server. To reconnect, just run client.py again.
