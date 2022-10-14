#why this work??????
def isPrime(n):
  if n==1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

primes = []
for p in range(1,5000):
  if isPrime(p)==True:
    primes.append(p)
max = 0
test = 0
i = 3
while True:
  test+=primes[i]
  if test>1000000:
    if isPrime(test)==True:
      print(max)
      break
  else:
    max = test
  i+=1