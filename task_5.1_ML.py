import socket

# url_input = input('Please enter URL to open: ')
url_input = 'https://docs.python.org/3/library/socket.html'
parts = url_input.split('/')
url_protocol = ['https:', 'http:']

if not parts[0] in url_protocol:
    host = parts[0]
else:
    host = parts[2]

# print(host)

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((host, 80))
cmd = ('GET ' + url_input + ' HTTP/1.0\r\n\r\n').encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    my_string = data.decode()

print(my_string)

mysock.close()

# print(host)
