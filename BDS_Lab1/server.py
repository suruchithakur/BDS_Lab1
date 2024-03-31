import socket
import threading

class ClientThread(threading.Thread):
    def __init__(self, client_socket, client_address, client_id):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.client_address = client_address
        self.client_id = client_id

    def run(self):
        print("Client", self.client_id, "connected from", self.client_address)
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print("Received from client", self.client_id, ":", message)
                    broadcast(message)
            except:
                print("Client", self.client_id, "disconnected.")
                clients.remove(self.client_socket)
                break

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            client.close()
            clients.remove(client)

def start_server():
    global clients
    clients = []

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server started. Listening on port 12345...")

    client_id = 1
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = ClientThread(client_socket, client_address, client_id)
        client_thread.start()
        clients.append(client_socket)
        client_id += 1

if __name__ == "__main__":
    start_server()
