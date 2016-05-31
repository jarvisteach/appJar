message = "this is a string with some xyz"
print(message)
message = [ord(c) for c in message]
print(message)
message = [x+5 for x in message]
print(message)

#for x in range(len(message)):
#      if message[x] > 122:
#            message[x] = message[x] - 26
#            print(message)

message = [ a-26 if a>122 else a for a in message]
message = [ a+26 if a<97  else a for a in message]

message = [chr(z) for z in message]
print(message)
