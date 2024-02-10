import socket
import threading

HEADER = 16
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = "UTF-8"
DISCONNECT_MESSAGE = "End"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_clients(conn, addr):
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
            vowel_count = 0
            for i in msg: 
                if i in 'aeiouAEIOU':
                    vowel_count += 1
                
            if vowel_count == 0:
                conn.send("Not enough vowel".encode(FORMAT))
            elif vowel_count <= 2:
                conn.send("Enough vowel I guess".encode(FORMAT))
            else:
                conn.send("Too many vowel".encode(FORMAT))
            
    conn.close()      

def start():
    server.listen()
    print("Server is listening")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clients, args=(conn, addr))
        thread.start()
        print(f"Total clients connected currently: {threading.active_count() - 1}")


start()