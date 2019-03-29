from socket import socket

serverName = 'enigma-decoder.local'
serverPort = 31319

clientSocket = socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

sentence = input("Input lowercase sentence:")
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)

clientSocket.close()
