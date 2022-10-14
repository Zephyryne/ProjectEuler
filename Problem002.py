ans = 0
a = 0
b = 1
while (a+b)<=4000000:
  c = a+b
  a = b
  b = c
  if c%2==0:
    ans+=c
print(ans)