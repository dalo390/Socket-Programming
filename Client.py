import socket
import time
import random

"""connect to robot"""
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ("Socket successfully created")

address = 'localhost'
port = 3310

client.connect((address, port))

client.sendall(b"ddo39")

from_server = client.recv(1024).decode()

print (from_server)
##################################
"""create a second socket to accept TCP connection from ROBOT"""
client2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket created to accept new connection
print ("Second socket successfully created")
port = int(from_server)
print(port)
time.sleep(1)

host = socket.gethostbyname(address)
client2.bind((host,port)) #bind socket to port number given by ROBOT
client2.listen(5) #listening for connection

s2, addr = client2.accept() #accepting socket into s2

from_server2 = s2.recv(1024).decode() #accepted socket receives numbers

print ("12 character string received is:", str(from_server2))
##################################
"""split 12 char string received into 2 variables"""
ports = str(from_server2)
portsList= ports.split(",")
port1 = int(portsList[0])
port2 = int(portsList[1])
print(port1, "and", port2)

address = (host, port1)
address2 = (host, port2)

"""create socket s3 and random variable num"""
s3 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP socket created
num = random.randrange(6,9)
print(num)

s3.bind(address2)
s3.sendto(str(num).encode(),address)
    
s3.settimeout(12.0)
    
data, server = s3.recvfrom(4096)
print(data)
    
"""send variable number to ROBOT"""
for i in range(4):
    s3.sendto(data,address)
    time.sleep(1)
print("complete")