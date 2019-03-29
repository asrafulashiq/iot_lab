import socket
import sys

serverName = 'enigma-decoder.local'
serverPort = 31319

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    clientSocket.connect((serverName, serverPort))
except socket.error as msg:
    print('Connection failed: ' + msg[1])
    sys.exit()

sentence = input("Input lowercase sentence:")
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)

clientSocket.close()
