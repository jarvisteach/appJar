import socket, sys

port = 9999
host =  socket.gethostbyname(socket.gethostname())

try:
      print ( "Opening socket:", host + ":" + str(port) )
      sock = socket.socket()
      sock.bind((host, port))
      sock.listen(5) # start listening, backlog of 5
      sock.settimeout(0.1)

      while True:
            try:
                  c, addr = sock.accept()
                  print ( "Got connection from:", addr)


                  while True:
                        print ( "looking for chunks" )
                        chunks = []
                        mess = ""
                        gotMessage = False
                        while True:
                              chunk = c.recv(1024)
                              if len(chunk) > 0:
                                    print ( "processing chunks" )
                                    if len(chunk) == 1 and ord(chunk) == 24: break
                                    chunks.append(chunk)
                                    gotMessage = True
                              else:
                                    print("Nothing")
                                    break
                        if gotMessage:
                              mess = b''.join(chunks).decode()
                              print( "Received: <", mess, ">")
                              outMsg = "Hi!"
                              c.sendall(outMsg.encode())
                              print( "Sent: ", outMsg )
                              gotMessage = False
                        else:
                              c.sendall(str(chr(24)).encode('ascii') )
            except Exception as e:
                  print(e)
            finally:
                  #c.close()
                  pass
finally:
      #c.close()
      pass
      sock.close()
