ans = 0

#for i in range(3,1001):
#    maximum = 0
#    for j in range(i**2):
#        check = ((i-1)**j + (i+1)**j) % (i**2)
#        if check > maximum:
#            maximum = check
#    ans += maximum

for i in range(3,1001):
    ans += i*(i-1)

print(ans)


# analysis
# (a-1)^1 + (a+1)^1 mod a^2 = 2a
# (a-1)^2 + (a+1)^2 mod a^2 = 2
# (a-1)^3 + (a+1)^3 mod a^2 = 6a
# (a-1)^4 + (a+1)^4 mod a^2 = 2
# (a-1)^5 + (a+1)^5 mod a^2 = 10a
# for a = 3: (a-1)^3 + (a+1)^3 mod a^2 = 6, 2, 18, etc. 6 is max
# for a = 4: (a-1)^3 + (a+1)^3 mod a^2 = 8, 2, 24, 40, 52, 72, etc. 12 is max
# max is n(n-1)?
