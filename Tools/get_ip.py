import socket
# How to get the IP address of a client using socket module

host_name = socket.gethostname()
ipaddress = socket.gethostbyname(host_name)
print('Your Computer Name is: '+host_name)
print('Your Computer IP Address is: ' + ipaddress)
