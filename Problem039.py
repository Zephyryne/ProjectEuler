maximum = 0
ans = 0

for i in range(1,1001):
    count = 0
    for a in range(1, int(i/3 + 1)):
        for b in range(a + 1,int((i - a)/2 + 1)):
            if a**2 + b**2 == (i - (a+b))**2:
                #print(str(a)+","+str(b)+","+str(c))
                count += 1
    if count > maximum:
        maximum = count
        ans = i

print(maximum)
print(ans)
