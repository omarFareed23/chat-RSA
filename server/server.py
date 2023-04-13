import socket
import os
from dotenv import load_dotenv
import sys
sys.path.append('..')
from RSA import encrypt, decrypt

##### load envs #####
load_dotenv()
#####################

### connection port ### 
HOST = 'localhost'
PORT = 5000
#######################


### public key ### 
n_client = int(os.getenv('N_CLIENT'))
d_client = int(os.getenv('D_CLIENT'))
###################

### private key ###
e_server = int(os.getenv('E_SERVER'))
d_server = int(os.getenv('D_SERVER'))
n_server = int(os.getenv('N_SERVER'))
#################

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

while True:
    # Receive data from the client
    data = client_socket.recv(1024).decode()

    if not data:
        break

    # Print the received message
    print(data)
    print('Received message:', decrypt(data, d_client, n_client))

    # Send a response back to the client
    response = encrypt(input('Enter response: '), e_server, n_server)
    client_socket.sendall(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
