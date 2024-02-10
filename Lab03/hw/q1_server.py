import socket

HEADER = 16
PORT = 5050
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
        conn.send("\nGoodbye".encode(FORMAT))
    else:
        msg = int(msg)
        salary = 1  

        if msg <= 40:
            salary = 200 * msg
            conn.send(f"\nClient's salary is {salary}".encode(FORMAT))
        elif msg > 40:
            salary = 8000 + (msg - 40) * 300
            conn.send(f"\nClient's salary is {salary}".encode(FORMAT))
      
conn.close() 

