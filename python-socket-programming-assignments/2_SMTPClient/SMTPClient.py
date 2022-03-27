from socket import *

endmsg = '\r\n.\r\n'

# Choose a mail server and call it mailserver and choose its port
mailserver = input('Enter mailserver hostname>> ')
port = 587

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, port))
recv = clientSocket.recv(1024).decode()
print(recv, end = '')
if recv[:3] != '220':
    print('220 reply not received from server.')
    exit()

# Send HELO command and print server response.
heloCommand = input('Say HELO...>> ')
heloCommand += '\r\n'
clientSocket.send(heloCommand.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end = '')
if recv[:3] != '250':
    print('250 reply not received from server.')
    exit()

# Send 'STARTTLS' command and print server response
startTLS = input('Enter STARTTLS command>> ')
startTLS += '\r\n'
clientSocket.send(startTLS.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end = '')
if recv[:3] != '555':
    print('555 reply not received from server.')
    exit()

# Send 'AUTH LOGIN' command and print server response
authLogin = input('AUTH LOGIN command   >> ')
authLogin += '\r\n'
clientSocket.send(authLogin.encode())
print(clientSocket.recv(1024).decode(), end = '')

# Send your username and password for auth
username = input('Enter username>> ')
username += '\r\n'
clientSocket.send(username.encode())
print(clientSocket.recv(1024).decode(), end = '')
password = input('Enter password>> ')
password += '\r\n'
clientSocket.send(password.encode())
print(clientSocket.recv(1024).decode(), end = '')

# Send 'MAIL FROM' command and print server response
mailFrom = input('MAIL FROM command>> ')
mailFrom += '\r\n'
clientSocket.send(mailFrom.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end = '')
if recv[:3] != '250':
    print('250 reply not received from server.')
    exit()

# Send 'RCPT TO' command and print server response
rcptTo = input('RCPT TO command>> ')
rcptTo += '\r\n'
clientSocket.send(rcptTo.encode())
recv = clientSocket.recv(1024).decode()
print(recv, end = '')
if recv[:3] != '250':
    print('250 reply not received from server.')
    exit()

# Send 'DATA' command and print server response
clientSocket.send((input('DATA command>> ') + '\r\n').encode())
recv = clientSocket.recv(1024).decode()
print(recv, end = '')
if recv[:3] != '354':
    print('354 reply not received from server')
    exit()

# Send message headers and print server response
print('Enter Headers>>')
data = input('FROM: ')
data += '\r\n'
data += input('TO: ')
data += '\r\n'
data += input('SUBJECT: ')
data += '\r\n'
clientSocket.send(data.encode())

# Send message body
clientSocket.send((input('Enter msg>> ')).encode())

# Message ends with a single period
clientSocket.send(input())

# Send 'QUIT' command and get server response
quit = input()
quit += '\r\n'
clientSocket.send(quit.encode())

recv = clientSocket.recv(1024).decode()
print(recv, end = '')
if recv[:3] != '221':
    print('221 reply not received from server')
    exit()
