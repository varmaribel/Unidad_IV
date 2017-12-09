import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8000))
message = "Mi nombre es Maribel & Daniela"
s.send(message.encode('utf-8'))
data = s.recv(1024)
print ('Received from server', data)
s.close()

print('Client is disconnected')

