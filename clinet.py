import socket

# Define host and port
HOST = 'localhost'
PORT = 5000

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

while True:
    # Get user input
    message = input('Enter message: ')

    # Send the message to the server
    client_socket.sendall(message.encode())

    # Receive the server's response
    data = client_socket.recv(1024).decode()

    # Print the response
    print('Received response:', data)

# Close the connection
client_socket.close()
