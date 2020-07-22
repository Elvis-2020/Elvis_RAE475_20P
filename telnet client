import telnetlib #bibliotēka

HOST = '127.0.0.1' #attālinātais serveris
PORT = 10023
timeout = 100 

tn = telnetlib.Telnet(HOST, PORT) #define interface
tn.set_debuglevel(100) #bug līmneis
data = tn.read_until("custom server", timeout=1) #define parameter
print "Data: " + data #datu izvade

tn.close() 
