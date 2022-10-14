from math import factorial

ans = 0

def factsum(x):
    new = 0
    for digit in str(x):
        new += factorial(int(digit))
    return new

for i in range(1,1000000):
    calc = i
    check = {calc}
    while factsum(calc) not in check:
        check.add(factsum(calc))
        calc = factsum(calc)
    if len(check) == 60:
        ans += 1

print(ans)


# Takes a while
