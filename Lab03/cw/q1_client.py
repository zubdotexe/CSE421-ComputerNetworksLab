import socket

HEADER = 17
PORT = 5051
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
  
send("Hello server")  
send(f"client's IP address is {SERVER} and client's device name is {socket.gethostname()}")

send(DISCONNECT_MESSAGE)