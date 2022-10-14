ans = 0

for i in range(100):
    check = 0
    while len(str(check**i)) <= i:
        check += 1
        if len(str(check**i)) == i:
            ans += 1

print(ans)
