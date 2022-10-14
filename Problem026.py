max = 0

def isPrime(n):
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

for i in range(1,1000):
    digits = 0
    divisible = 9
    if isPrime(i) == True and len(str(round(1/i,15))) == 17:
        while True:
            if divisible%i == 0:
                break
            else:
                divisible = divisible*10 + 9
                digits += 1
    if digits > max:
        max = digits
        value = i

print(value)
