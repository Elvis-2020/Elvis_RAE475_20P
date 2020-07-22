from ftplib import FTP #bibliotēka

ftp = FTP('') 
ftp.connect('localhost',1026) 
ftp.login() 
ftp.cwd('/home/elvish/ftp')  
ftp.retrlines('LIST') 

def uploadFile():
 filename = 'testfile.txt' #faila nosaukums
 ftp.storbinary('STOR '+filename, open(filename, 'rb')) #faila glabātuves tipa norāde
 ftp.quit() #opcijas pārtraukšana

def downloadFile():
 filename = 'testfile.txt' 
 localfile = open(filename, 'wb')
 ftp.retrbinary('RETR ' + filename, localfile.write, 1024) #lejuplādes faila tips
 ftp.quit() #opcijas pātraukšana
 localfile.close() #sesijas noilgums

uploadFile()
