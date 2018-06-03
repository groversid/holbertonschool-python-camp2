#!/usr/bin/env python3
def uppercase(string):
   for i in string:
      if (ord(i)>96 and ord(i)<123):
         i = chr(ord(i) - 32)
         print("{}".format(i), end="")
      print("")
