from socket import *
from lc_constants import *

serverName = "192.168.0.125"

serverPort = HANDSHAKE_PORT
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

clientSocket.send("Incoming client".encode())
playPortStr = clientSocket.recv(2048).decode()
clientSocket.close()
clientSocket .connect(Int(playPortStr))
print("Message received: '{}'".format(modifiedMessage.decode()))
clientSocket.close()
print("Client socket closed.")