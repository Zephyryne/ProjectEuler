def isPrime(n):
    if n < 0:
        return False
    if n==1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

nums = []
checker = []
for i in range(1,1000001):
    if isPrime(i) == True:
        nums.append(i)
        checker.append(i)

for num in nums:
    digits = len(str(num))
    if digits > 1:
        for j in range(1,digits):
            probe = int(str(num)[j:]+str(num)[:j])
            if probe not in nums:
                checker.remove(num)
                break

print(len(checker))
