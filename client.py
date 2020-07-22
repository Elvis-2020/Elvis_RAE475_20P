#coding
import socket 

HOST = '127.0.0.1' 	
PORT = 50007      
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Connecting...') 
s.connect((HOST, PORT)) 
s.sendall(b'Hello, world')
data = s.recv(1024) 
s.close() 
print('Received', repr(data)) 