import socket
import threading
import tkinter as tk
from tkinter import messagebox

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode()
            chat_text.insert(tk.END, message + '\n')
        except:
            print("Disconnected from server.")
            break

def send_message(event=None):
    message = message_entry.get()
    if message:
        try:
            client_socket.send(message.encode())
            message_entry.delete(0, tk.END)
        except Exception as e:
            print("Error sending message:", e)
            messagebox.showerror("Error", "Failed to send message. Please try again.")

def start_client():
    global client_socket

    root = tk.Tk()
    root.title("Chat Client")

    chat_frame = tk.Frame(root)
    chat_frame.pack(padx=10, pady=10)

    scrollbar = tk.Scrollbar(chat_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    global chat_text
    chat_text = tk.Text(chat_frame, wrap=tk.WORD, yscrollcommand=scrollbar.set)
    chat_text.pack(expand=True, fill=tk.BOTH)
    scrollbar.config(command=chat_text.yview)

    global message_entry
    message_entry = tk.Entry(root, width=50)
    message_entry.pack(side=tk.LEFT, padx=10, pady=10)
    message_entry.bind("<Return>", send_message)

    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack(side=tk.RIGHT, padx=10, pady=10)

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(('localhost', 12345))
        print("Connected to server.")
    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running and reachable.")
        messagebox.showerror("Error", "Failed to connect to server. Please make sure the server is running.")
        return

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    root.mainloop()

if __name__ == "__main__":
    start_client()
