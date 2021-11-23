import socket

ip = socket.gethostbyname('www.google.com.ar')
print(ip)

#google1
hostByAddress = socket.gethostbyaddr('142.250.79.67')
print(hostByAddress)

#google2
hostByAddress2 = socket.gethostbyaddr('142.250.79.68')
print(hostByAddress2)

hostAlternativeNames = socket.getfqdn('eze06s11-in-f3.1e100.net')
print(hostAlternativeNames)

#github, no 3unciona
# hostByAddress3 = socket.gethostbyaddr('20.201.28.151')
# print(hostByAddress3)

# Mi PC y su IP privado
myHost = socket.gethostname()
print (myHost)

myIp = socket.gethostbyname(myHost)
print(myIp)

# mi IP público, el hostname es porque tengo contratado por fibertel
hostByAddressMine = socket.gethostbyaddr('201.231.193.21')
print(hostByAddressMine)

hostByAddressMine = socket.gethostbyaddr('69.59.196.211')
print(hostByAddressMine)

