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

    print(message)
    print(message.split()[1])
    filename = message.split()[1].partition("/")[2]
    print(filename)
    fileExist="false"
    filetouse="/"+filename
    print(filetouse)
    try:
        f = open(filename,"rb")
        outputdata = f.read()
        fileExist = "true"
        connectionsocket.send(b"HTTP/1.0 200 OK \r\n")
        connectionsocket.send(b"Content-Type:text/html\r\n")
        connectionsocket.send(outputdata+b'\r\n')
        connectionsocket.close()

        print('Read from cache')

    except IOError:
        if fileExist =="false":
            c = socket(AF_INET, SOCK_STREAM)
            hostn = filename.replace("www.","",1)
            print(hostn)
            try:
                c.connect((hostn, 80))
                fileobj = c.makefile('r', 80)
                fileobj.write("GET http://"+filename+"HTTP/1.0\r\n")
                buffer = fileobj.readlines()
                tempfile = open("./"+filename,"wb")
                for i in buffer:
                    tempfile.write(i)
                    connectionsocket.send(i)
                    c.close()
            except:
                print("Illegal request")
                c.close()
        else:
            connectionsocket.send("HTTP/1.0 404 Not found error\r\n")
            connectionsocket.send("Content-Type:text/html\r\n\r\n")
            

    connectionsocket.close()
    


                
            



