import socket

#####################################
## Network classes
#####################################
class net:
      # connect to the spcified host on the specified port
      # if only 1 parameter is provided, it is assumed to be the port
      def __init__(self, host, port=None):

            # allows user to pass in only a port, and we use our own IP address
            if port is None:
                  port = host
                  host = self.getIPAddress()
                  if host == None: host="localhost"

            self.host = host
            self.port = port
            self.timeout = 0.01
            self.connected = False

            self.__connect()

      # connect to the configured host & port
      def __connect(self):
            if self.connected: return True
            try:
                  self.sock = socket.socket()
                  self.sock.connect( (self.host, self.port) )
                  self.sock.settimeout(self.timeout)
                  self.connected = True
                  return True
            except Exception as e:
                  self.close()
            return False

      # get the current IP address
      def getIPAddress(self):
            return socket.gethostbyname(socket.gethostname())

      # send a message to the server
      def sendMessage(self, msg):
            try:
                  if self.__connect():
                        self.sock.sendall(msg.encode('ascii') )
                        return True
            except Exception as e:
                  self.close()
            return False

      # send a 'ping' to the server, uses TCP to send a control character
      # only really checks if the socket is still alive
      def ping(self):
            try:
                  if self.__connect():
                        self.sock.sendall(str(chr(24)).encode('ascii') )
                        return True
            except Exception as e:
                  self.close()
            return False

      # get a message from the server
      # will ignore a ping, and send a ping back if received
      def getMessage(self):
            try:
                  if self.__connect():
                        recv = self.sock.recv(1024).decode()
                        if ord(recv[0]) == 24:
                              return None
                        else:
                              self.ping()
                              return recv
            except Exception as e:
                  pass
            return None

      # close the connection
      def close(self):
            self.sock.close()
            self.connected = False

if __name__ == "__main__":
      print("Testing NET Class")
      myNet = net(777)
      print("Connected to myself: ", myNet.getIPAddress())
      print("Listening on port: ", myNet.port)
      while True:
            print(myNet.getMessage())
