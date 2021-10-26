# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
  serverSocket = socket(AF_INET, SOCK_STREAM)
  #Prepare a server socket
  serverSocket.bind(("localhost", port))
  #Fill in start
  serverSocket.listen(5)
  #Fill in end

  while True:
    #Establish the connection
    #print('Ready to serve...')
    #connectionSocket, addr = #Fill in start      #Fill in end
    connectionSocket, addr = serverSocket.accept()
    try:
      request = connectionSocket.recv(1024).decode()
      #print(request)
      try:
        #message = #Fill in start    #Fill in end
        message = request.split('\n')[0]
        #print(message)
        filename = message.split()[1]
        #print(filename)
        f = open(filename[1:])
        #outputdata = #Fill in start     #Fill in end
        outputdata = f.read()
        f.close()
        
        #Send one HTTP header line into socket.
        #Fill in start
        #outputdata = 'HTTP/1.0 200 OK\n\n' + outputdata
        #connectionSocket.send("HTTP/1.0 200 OK\n".encode())
        #connectionSocket.send("Content-Type: text/html\n".encode())
        connectionSocket.sendall(str.encode("HTTP/1.0 200 OK\n",'iso-8859-1'))
        connectionSocket.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
        connectionSocket.send(str.encode('\r\n'))

        #print(outputdata)
        #Fill in end

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
          connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())
        connectionSocket.close()
      except IOError:
        # Send response message for file not found (404)
        #Fill in start
        #outputdata = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'
        connectionSocket.sendall(str.encode("HTTP/1.0 404 NOT FOUND\n\nFile Not Found",'iso-8859-1'))
        connectionSocket.send(str.encode('\r\n'))
        #Fill in end


        #Close client socket
        #Fill in start
        #connectionSocket.sendall(outputdata.encode())
        connectionSocket.close()
        #Fill in end

    except (ConnectionResetError, BrokenPipeError):
      pass

  serverSocket.close()
  sys.exit()  # Terminate the program after sending the corresponding data

if __name__ == "__main__":
  webServer(13331)