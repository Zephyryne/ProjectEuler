primes = []
compo = []

def isPrime(n):
  if n==1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n%i==0:
      return False
  return True

for i in range(3,10000):
    if isPrime(i):
        primes.append(i)
    elif i%2 == 1:
        compo.append(i)

for num in compo:
    for prime in primes:
        add = 0
        test = prime
        while test < num:
            test = prime + 2*(add**2)
            add += 1
        if test == num:
            break
        elif test > num and prime > num:
            print(num)
            break

#just stop the code manually once it spits out the first response (5777)
