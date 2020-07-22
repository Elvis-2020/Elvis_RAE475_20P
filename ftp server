from pyftpdlib.authorizers import DummyAuthorizer #bibliotēka
from pyftpdlib.handlers import FTPHandler 
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer() #lietotāju klase
authorizer.add_user("rus_sud", "12345", "/home/russud/ftp", perm="elradfmw") #definē lietotāju
authorizer.add_anonymous("/home/russud", perm="elradfmw") #nedefinēts lietotājs

handler = FTPHandler #autorizācijas veids
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler) #definē serveri
server.serve_forever() 
