def isPrime(n):
  if n==1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True
  
sum = 0
num = 1
while num<2000000:
  if isPrime(num)==True:
    sum+=num
  num+=1
print(sum)