import SocketServer 
from telnetsrv.threaded import TelnetHandler, command #library
class MyHandler(TelnetHandler): #klases parametri

    WELCOME = "HI from Elvis's server"
    @command('version')
    def version(self, params):
     self.writeresponse("V1.0")

class TelnetServer(SocketServer.TCPServer): #define server
    allow_reuse_address = True
    

server = TelnetServer(("0.0.0.0", 10023), MyHandler) #define server
server.serve_forever() 
