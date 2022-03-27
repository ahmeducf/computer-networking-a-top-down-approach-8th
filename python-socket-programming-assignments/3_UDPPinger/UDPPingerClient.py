import sys, time
from socket import *

argv = sys.argv                      
host = argv[1]
port = argv[2]

serverName = argv[1]
serverPort = int(argv[2])
timeout = 1 # in second

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(timeout)

pTime = 0   # Sequence number of the ping message

# Ping for 10 times
while pTime < 10:
    pTime += 1
    pingMessage = "Ping " + str(pTime) + " " + time.asctime()
    try:
        sendTime = time.time()
        clientSocket.sendto(pingMessage.encode(), (serverName, serverPort))
        responseMessage, serverAddress = clientSocket.recvfrom(2048)
        recvTime = time.time()
        RTTDuration = recvTime = sendTime
        print("Reply from " + serverAddress[0] + ": " + responseMessage.decode())
        print("RTT: " + str(RTTDuration) + '\n')
    except:
        print("Request timed out\n")
        continue

clientSocket.close()