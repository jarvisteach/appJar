import socketserver

class MyTCPHandler(socketserver.BaseRequestHandler):

      def handle(self):
            self.data = self.request.recv(1024).strip()
            print("Received:",self.client_address[0], ",:",self.data)
            self.request.sendall(self.data.upper())
            print("Message sent...")

if __name__ == "__main__":
      HOST, PORT = "localhost", 9999

      # Create the server, binding to localhost on port 9999
      server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

      # Activate the server; this will keep running until you
      # interrupt the program with Ctrl-C
      server.serve_forever()
