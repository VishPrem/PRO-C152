import socket
from threading import Thread

nickname = input("Please enter your nickname: ")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address = "127.0.0.1"
port = 8000
client.connect((ip_address, port))

def receive():
    while True:
        try:
            message = client.recv(2048).decode("utf-8")
            if message == "NICKNAME":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            print("An error has occured.")
            client.close()
            break

def write():
    while True:
        message = input()
        client.send(message.encode("utf-8"))

recieve_thread = Thread(target=receive)
recieve_thread.start()

write_thread = Thread(target=write)
write_thread.start()
