#import socket module
from socket import *
import sys      # In order to terminate the program



serverPort = 4500

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

while True:
    # Establish the connection
    print('Ready to serve…')
    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(2048).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        # Send one HTTP response line into socket
        connectionSocket.send("\r\nHTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        f.close()

    except IOError:
        # Send response message for file not found
        connectionSocket.send("\r\nHTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        # Close client connection socket
        connectionSocket.close()
    
serverSocket.close()
sys.exit()  #Terminate the program after sending the corresponding data