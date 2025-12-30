from socket import * 
import base64
import ssl 
username = ""
password = ""


msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
mailserver= "smtp.gmail.com"
mailport =465
sslcontext =ssl.create_default_context()

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket = sslcontext.wrap_socket(clientSocket, server_hostname=mailserver)
clientSocket.connect((mailserver, mailport ))


recv = clientSocket.recv(1024).decode()
if(recv[:3]!='220'):
    print('220 reply not received from server')
helocommand = 'HELO Sujal\r\n'
clientSocket.send(helocommand.encode())
recv1 = clientSocket.recv(1024).decode()
if(recv1[:3]!='250'):
    print('250 reply not received from server')



clientSocket.send(b'AUTH LOGIN\r\n')
recv_auth= clientSocket.recv(1024).decode()
print(recv_auth)

clientSocket.send(base64.b64encode(username.encode())+b'\r\n')
recv_user = clientSocket.recv(1024).decode()
print(recv_user)

clientSocket.send(base64.b64encode(password.encode())+b'\r\n')
recv_pass = clientSocket.recv(1024).decode()
print(recv_pass)

message1 = 'MAIL FROM:<sujalgyawali4@gmail.com>\r\n'
clientSocket.send(message1.encode())
recv2 = clientSocket.recv(1024).decode()
if(recv2[:3]!='250'):
    print('250 reply not received')

message2 = 'RCPT TO:<sgyawali66@gmail.com>\r\n'
clientSocket.send(message2.encode())
recv3 = clientSocket.recv(1024).decode()
if(recv3[:3]!='250'):
    print('250 reply not received')

message3 = 'DATA\r\n'
clientSocket.send(message3.encode())
recv4 = clientSocket.recv(1024).decode()
if(recv4[:3]!='354'):
    print('354 reply not received')

clientSocket.send(msg.encode()+endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
if(recv5[:3]!='250'):
    print("250 not received")

clientSocket.send("QUIT\r\n".encode())
recv6 = clientSocket.recv(1024).decode()
if(recv6[:3]!='221'):
    print("Closing Conncetion")



