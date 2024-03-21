"""
f= open("test.txt", "w") # 'w' , 'a',  'r' w= override a =append r= read
f.write("#This is the first line\n")
f.write("*#This is the second line")
f.close
"""

with open("test.tx", "w") as f:
    f.write("first line\n")
    f.write("second line\n")
f.close

print(dir(f))

try:
  with open("test.tx", "w") as f:
    f.readline
except Exception as e:
   print(e)
f.close

try:
  with open("test.tx", "w") as f:
    f.readline
except ('please check the fine name'):
   print(e)