import socket  

localIP     = "127.0.0.1" 
localPort   = 20001  
bufferSize  = 1024 
msgFromServer       = "Hello UDP Client" #ziņojuma izvade
bytesToSend         = str.encode(msgFromServer)  

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM) #socket parameters
UDPServerSocket.bind((localIP, localPort)) #IP piesaiste
print("UDP server up and listening") #ziņojuma izvade

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message) 
    clientIP  = "Client IP Address:{}".format(address) #define parameters
    print(clientMsg) #ziņojuma izvade
    print(clientIP) #ziņojuma izvade
    UDPServerSocket.sendto(bytesToSend, address)
