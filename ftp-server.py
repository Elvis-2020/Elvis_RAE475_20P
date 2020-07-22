from pyftpdlib.authorizers import DummyAuthorizer #bibliotēka
from pyftpdlib.handlers import FTPHandler 
from pyftpdlib.servers import FTPServer

authorizer = DummyAuthorizer() #lietotāju klase
authorizer.add_user("elvish", "12345", "/home/elvish/ftp", perm="elradfmw") #definē lietotāju
authorizer.add_anonymous("/home/elvish", perm="elradfmw") #nedefinēts lietotājs

handler = FTPHandler #autorizācijas veids
handler.authorizer = authorizer

server = FTPServer(("127.0.0.1", 1026), handler) #definē serveri
server.serve_forever() 
