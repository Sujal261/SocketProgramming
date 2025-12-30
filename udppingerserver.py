from socket import * 
import sys 
import random 

serverName ="localhost"
serverPort = 12000 
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("Server is listening")
while True:
    num = random.randint(0,10)
    message, client= serverSocket.recvfrom(1024)
    messagedecoded = message.decode().upper()
    if(num<4):
        continue
    serverSocket.sendto(messagedecoded.encode(), client)


