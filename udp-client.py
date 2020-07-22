import socket #library

msgFromClient       = "Hello UDP Server"  
bytesToSend         = str.encode(msgFromClient)  
serverAddressPort   = ("127.0.0.1", 20001) #interface parameters
bufferSize          = 1024 

UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #socket parameters
UDPClientSocket.sendto(bytesToSend, serverAddressPort) #sending parameters
msgFromServer = UDPClientSocket.recvfrom(bufferSize) #servera ziņojums
msg = "Message from Server {}".format(msgFromServer[0]) #ziņojums

print(msg) #ziņojuma izvade
