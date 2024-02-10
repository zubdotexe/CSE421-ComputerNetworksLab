import socket

HEADER = 17
PORT = 5051
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

server.listen()
print("server is listening")

conn, addr = server.accept()
connected = True

while connected:
  msg_len = conn.recv(HEADER).decode(FORMAT)
  if msg_len:
    msg_len = int(msg_len)
    msg = conn.recv(msg_len).decode(FORMAT)
    
    if msg == DISCONNECT_MESSAGE:
      connected = False
      conn.send("Goodbye".encode(FORMAT))
    else:
      print(msg)
      conn.send("Message received".encode(FORMAT))
      
conn.close()      