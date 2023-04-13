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


### private key ### 
n_client = int(os.getenv('N_CLIENT'))
d_client = int(os.getenv('D_CLIENT'))
e_client = int(os.getenv('E_CLIENT'))
###################

### public key ###
d_server = int(os.getenv('D_SERVER'))
n_server = int(os.getenv('N_SERVER'))
#################


# Define host and port
HOST = 'localhost'
PORT = 5000

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

while True:
    # Get user input
    message = encrypt(input('Enter message: '), e_client, n_client)

    # Send the message to the server
    client_socket.sendall(message.encode())

    # Receive the server's response
    data = client_socket.recv(1024).decode()

    # Print the response
    print('Received response:', decrypt(data, d_server, n_server))

# Close the connection
client_socket.close()
