from socket import * 
import sys 
serverport = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverport))
serverSocket.listen(1)
print("Server is ready to serve")
while True:
    print("Ready to serve")
    connectionsocket , addr = serverSocket.accept()
    try:
        message = connectionsocket.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:],'rb')
        output_data = f.read()
        f.close()
        connectionsocket.send(b"HTTP/1.1 200 OK \r\n\r\n"+output_data)
        connectionsocket.send("\r\n".encode())
        connectionsocket.close()

    except IOError:
        connectionsocket.send(b"HTTP/1.1 404 Not Found\r\n\r\n")
        connectionsocket.send(b"<html><body><h1> 404 NOT FOUND </h1></body></html>")
        connectionsocket.close()


