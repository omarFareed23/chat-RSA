import socket
import sys
sys.path.append('..')
from RSA import encrypt, decrypt, generate_public_and_private_key

# Define host and port
HOST = 'localhost'
PORT = 5000

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

public_key, private_key = generate_public_and_private_key(64)
d_client, n_client = public_key
e_client, n_client = private_key
sent_public_key = f"{d_client}|{n_client}"
client_socket.sendall(sent_public_key.encode())
server_public_key = client_socket.recv(1024).decode().split("|")
server_public_key = list(map(int, server_public_key))

while True:
    # Get user input
    message = encrypt(input('Enter message: '), e_client, n_client)

    # Send the message to the server
    client_socket.sendall(message.encode())

    # Receive the server's response
    data = client_socket.recv(1024).decode()

    # Print the response
    print('Received response:', decrypt(data, server_public_key[0], server_public_key[1]))

# Close the connection
client_socket.close()
