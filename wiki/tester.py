while True:
      i = int(input("Choice: "))

      if 64 < i < 91:
            print("between 64&91")
            if i < 65:
                  print("lower than 65")
            else:
                  print("not lower than 65")
      elif 31 < i < 33:
            print("in 30s range")
      else:
            print("other")
            if i < 97:
                  print("less 97")
            else:
                  print("high 97")
