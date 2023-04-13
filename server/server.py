import socket
import sys
sys.path.append('..')
from RSA import encrypt, decrypt, generate_public_and_private_key

### connection port ### 
HOST = 'localhost'
PORT = 5000
#######################

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print('Server listening on {}:{}'.format(HOST, PORT))

# Wait for a connection
client_socket, client_address = server_socket.accept()

print('Connected by', client_address)

public_key, private_key = generate_public_and_private_key(64)
d_server, n_server = public_key
e_server, n_server = private_key
sent_public_key = f"{d_server}|{n_server}"
client_public_key = list(map(int,client_socket.recv(1024).decode().split("|")))
client_socket.sendall(sent_public_key.encode())

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode()

    if not data:
        break

    # Print the received message
    print('Received message:', decrypt(data, client_public_key[0], client_public_key[1]))

    # Send a response back to the client
    response = encrypt(input('Enter response: '), e_server, n_server)
    client_socket.sendall(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
