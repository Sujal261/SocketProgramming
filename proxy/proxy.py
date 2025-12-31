from socket import * 
import sys 
if(len(sys.argv)<=1):
    print("Usage :'python3 proxy.py server_ip'\n[server_ip]:It is the ip address of the proxy server")

    sys.exit(2)
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((sys.argv[1], 12000))
serverSocket.listen(1)
print("Serevr is ready")
while 1:
    print("Ready top serve...")
    connectionsocket,addr = serverSocket.accept()
    print(f"Received a connection from:{addr}")
    message = connectionsocket.recv(1024).decode()

   
    filename = message.split()[1].partition("/")[2]
  
    fileExist="false"
    filetouse="/"+filename
    try:
        f = open(filename,"rb")
        outputdata = f.read()
        f.close()
        fileExist = "true"
        connectionsocket.send(b"HTTP/1.1 200 OK \r\n\r\n"+outputdata)
        connectionsocket.send("\r\n".encode())
        connectionsocket.close()
        print('Read from cache')

    except IOError:
        if fileExist =="false":
            c = socket(AF_INET, SOCK_STREAM)
           
            try:
                c.connect(("localhost", 8000))
                request = f"GET /{filename} HTTP/1.0\r\n Host:localhost\r\n\r\n"
                c.send(request.encode())
                response = c.recv(1024)
                with open(filename, "wb") as tempfile:

                    tempfile.write(response)
                connectionsocket.send(response)
                c.close()
            except:
                print("Illegal request")
                c.close()
        else:
            connectionsocket.send("HTTP/1.0 404 Not found error\r\n")
            connectionsocket.send("Content-Type:text/html\r\n\r\n")
            

    connectionsocket.close()
    


                
            



