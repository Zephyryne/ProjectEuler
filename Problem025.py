ind = 1
a = 0
b = 1
c = 1
while len(str((a+b)))<1000:
  c = a+b
  a = b
  b = c
  ind+=1
print(ind+1)