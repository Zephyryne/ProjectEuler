num = 600851475143
i = 2
while i<=num:
  if num%i==0:
    max = i
    num = int(num/i)
  i+=1
print(max)