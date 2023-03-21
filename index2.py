import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind the socket to a public host and a port
server_socket.bind((host, port))

# queue up to 5 requests
server_socket.listen(5)

while True:
    # establish a connection
    client_socket, address = server_socket.accept()

    # receive data from the client
    data = client_socket.recv(1024)

    # process the data (store, delete, etc.)
    # ...

    # send a response to the client
    client_socket.send('Message received.'.encode())

    # close the client socket
    client_socket.close()
