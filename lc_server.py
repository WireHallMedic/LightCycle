from socket import *
from lc_constants import *

def connect():
   connectionSocket = None
   addr = None
   
   handshakePort = HANDSHAKE_PORT
   handshakeSocket = socket(AF_INET, SOCK_STREAM)
   handshakeSocket.bind(('', handshakePort))
   
   playPort = PLAY_PORT
   playSocket = socket(AF_INET, SOCK_STREAM)
   playSocket.bind(('', playPort))
   
   handshakeSocket.listen(1)
   
   print("Server listening")
   
   connectionSocket, addr = handshakeSocket.accept()
   message = handshakeSocket.recv(2048).decode()
   print("Connection received, switching to play socket")
   connectionSocket.send("{}".format(PLAY_PORT).encode())
   connectionSocket.close()
   print("handshake socket closed")
   
   connectionSocket, addr = playSocket.accept()
   print("Connected to play socket")
   

def process_message(msg):
   pass

if __name__ == "__main__":
   connect()