# It's just combo: 40C20

num = 1
for i in range(2,41):
  num*=i
denom = 1
for i in range(2,21):
  denom*=i
print(int(num/(denom**2)))
