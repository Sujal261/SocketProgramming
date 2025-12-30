from socket import * 
import sys 
import time 
serverName ="localhost"
serverPort= 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
randomstring ="asdfghjklm"
clientSocket.settimeout(1)
for i in range(10):
    message = randomstring[i]
    start_time = time.perf_counter()
    clientSocket.sendto(message.encode(), (serverName, serverPort))

    try:
        messagefromserver, serverAddr = clientSocket.recvfrom(1024)
        end_time = time.perf_counter()
        messagefromserver = messagefromserver.decode()
        print(f"{messagefromserver} RTT: {end_time - start_time:.6f} seconds")
    except timeout:
        end_time = time.perf_counter()
        print(f"{message} timed out after {end_time - start_time:.6f} seconds")


    




