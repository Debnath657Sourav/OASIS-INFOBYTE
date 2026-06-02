#server.py
import socket
import threading

HOST = '0.0.0.0'
PORT = 5000    #changed from 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

print(f"Server is running on port {PORT}...")

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()

            nickname = nicknames[index]
            nicknames.remove(nickname)

            broadcast(f"{nickname} left the chat!".encode())
            break

def receive():
    while True:
        client, address = server.accept()

        print(f"Connected with {str(address)}")

        client.send("NICK".encode())
        nickname = client.recv(1024).decode()

        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname: {nickname}")

        broadcast(f"{nickname} joined the chat!".encode())
        client.send("Connected to server!".encode())

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
#cilent.py
import socket
import threading

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = input("Enter Server IP: ")
PORT = 5000

client.connect((HOST, PORT))

def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "NICK":
                client.send(nickname.encode())
            else:
                print(message)

        except:
            print("An error occurred!")
            client.close()
            break

def write():
    while True:
        message = f"{nickname}: {input('')}"
        client.send(message.encode())

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
