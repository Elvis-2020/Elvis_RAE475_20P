import socket

HOST = ''                 
PORT = 50007              
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #define socket parameters
s.bind((HOST, PORT)) #norāda interfeisu un portu
print('Listening...') 
s.listen(1) #socket status
conn, addr = s.accept() #savienojuma akceptēšana
print('Connected by', addr) #ziņojuma izvade par lietotāju
while True: 
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data) #connection parameters
conn.close() #savienojuma pārtraukšana
