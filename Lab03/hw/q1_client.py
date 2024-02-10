import socket
import threading

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "End"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
  message = msg.encode(FORMAT)
  msg_len = len(message)
  send_len = str(msg_len).encode(FORMAT)
  send_len += b' ' * (HEADER - len(send_len))
  
  client.send(send_len)
  client.send(message)
  print(client.recv(2048).decode(FORMAT))
  

connected = True

while connected:
    input_message = input("Please enter the amount of hours you've worked: \n")
    
    if input_message == "Done":
        send(DISCONNECT_MESSAGE)
        connected = False
    else:
        send(input_message)

