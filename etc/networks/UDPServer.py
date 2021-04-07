import socket


localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024


msgFromServer = "Hello UDP Client"

bytesToSend = str.encode(msgFromServer)


# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# If zero is given, the socket is put in non-blocking mode. If None is given, the socket is put in blocking mode
# UDPServerSocket.settimeout(0)  
UDPServerSocket.setblocking(0)     

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))


print("UDP server up and listening")


# Listen for incoming datagrams

while(True):
    bytesAddressPair = None
    try:
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    except BlockingIOError:
        pass

    if bytesAddressPair:
        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)

        print(clientMsg)
        print(clientIP)

    # Sending a reply to client

        UDPServerSocket.sendto(bytesToSend, address)
    # print('check sum')
