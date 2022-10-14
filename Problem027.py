def isPrime(n):
    if n < 0:
        return False
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

tops = 0
mult = 0

for a in range(2,1000):
    if isPrime(a) == True:
        for b in range(2,1000):
            if isPrime(b) == True:
                n = 0
                while True:
                    if isPrime((n**2)+(a*n)+(b)) == True:
                        n += 1
                    else:
                        if n > tops:
                            tops = n
                            mult = a * b
                        break
                n = 0
                while True:
                    if isPrime((n**2)-(a*n)+(b)) == True:
                        n += 1
                    else:
                        if n > tops:
                            tops = n
                            mult = 0 - (a * b)
                        break

                n = 0
                while True:
                    if isPrime((n**2)+(a*n)-(b)) == True:
                        n += 1
                    else:
                        if n > tops:
                            tops = n
                            mult = 0 - (a * b)
                        break
                n = 0
                while True:
                    if isPrime((n**2)-(a*n)-(b)) == True:
                        n += 1
                    else:
                        if n > tops:
                            tops = n
                            mult = a * b
                        break
print(mult)
