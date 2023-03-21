import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# connect to the server
client_socket.connect((host, port))

# send a message to the server
message = 'Hello, server!'
client_socket.send(message.encode())

# receive a response from the server
response = client_socket.recv(1024)

# display the response
print(response.decode())

# close the socket
client_socket.close()
