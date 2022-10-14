def isPrime(n):
  if n==1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True
  
count = 0
num = 1
while count<=10001:
  if isPrime(num)==True:
    count+=1
  if count!=10001:
    num+=1
  if count==10001:
    print(num)
    break