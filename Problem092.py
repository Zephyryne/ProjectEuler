count = 0

def sq(x):
    nxt = 0
    for digit in str(x):
        nxt += int(digit)**2
    return nxt

for i in range(1,10000000):
    test = i
    while sq(test) != 1 and sq(test) != 89:
        test = sq(test)
    if sq(test) == 89:
        count += 1

print(count)

# Takes a few minutes
