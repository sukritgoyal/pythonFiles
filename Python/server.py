import socket

# create a socket object
serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9999

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
   # establish a connection
   addr=serversocket.accept()
   print(addr)
   msg = 'Thank you for connecting'+ "\r\n"
   addr[0].send(msg.encode('ascii'))
   addr[0].close()
   
