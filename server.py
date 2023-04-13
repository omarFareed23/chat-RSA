import socket

# Define host and port
HOST = 'localhost'
PORT = 5000

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
    print('Received message:', data)

    # Send a response back to the client
    response = input('Enter response: ')
    client_socket.sendall(response.encode())

# Close the connection
client_socket.close()
server_socket.close()
