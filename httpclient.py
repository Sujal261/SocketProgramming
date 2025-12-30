from socket import * 
import sys 
args = sys.argv[1:]
serverName = "localhost"
serverPort = 12000 
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
request = f"GET /{args[0]} HTTP/1.1\r\n Host: localhost\r\n\r\n"
clientSocket.send(request.encode())
response = clientSocket.recv(1024).decode()
print("Response from server:\n")
print(response)
clientSocket.close()

