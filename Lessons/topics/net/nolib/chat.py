import socket, sys

HOST, PORT = "localhost", 9999
print ( socket.gethostbyname(socket.gethostname()) )


try:
      data = None
      while data != "QUIT":
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((HOST, PORT))
            data = input ( "Enter message:" )
            sock.sendall(data.encode('ascii') )

            received = sock.recv(1024)

            print( "Sent:     {}".format(data))
            print( "Received: {}".format(received))
            sock.close()
finally:
      sock.close()
