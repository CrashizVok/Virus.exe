import socket
# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# define the remote host and port
remote_host = "127.0.0.1"  # Módosítsd a távoli kiszolgáló címét vagy domainját
remote_port = 80 # Módosítsd a távoli kiszolgáló által használt portra

# establish a TCP connection with the remote host and port
s.connect((remote_host, remote_port))

# send a message to the remote host
message = "Hello, world!"
s.sendall(message.encode())

# close the socket
s.close()

