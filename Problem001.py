ans = 0
for i in range (0,1000):
  if i%3==0 and i%5!=0:
    ans+=i
  elif i%5==0 and i%3!=0:
    ans+=i
  elif i%3==0 and i%5==0:
    ans+=i
print(ans)