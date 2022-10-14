nums = []
for i in range(1,28124):
    nums.append(int(i))

def determine(n):
    sum = 0
    for j in range(1,int(n**0.5)+1):
        if n%j == 0:
            if j == 1:
                sum += 1
            elif n == j**2:
                sum += j
            else:
                sum += (j + (n/j))
        if sum > n:
            return True
abunds = []
for k in range(1,28124):
    if determine(k) == True:
        abunds.append(int(k))

for a in abunds:
    for b in abunds:
        if int(a+b) > 28123:
            break
        if int(a+b) in nums:
            nums.remove(int(a+b))

final = 0
for c in nums:
    final += c
print(final)
