for a in range(1,1001):
  for b in range(1,1001-a):
    c = 1000-(a+b)
    if c!=0 and (a**2)+(b**2)==(c**2):
      ans = a*b*c
print(ans)