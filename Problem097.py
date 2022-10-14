ans = 1

for i in range(1,7830458):
    ans *= 2
    if len(str(ans)) > 10:
        ans = int(str(ans)[-10:])

ans *= 28433
ans += 1
ans = int(str(ans)[-10:])

print(ans)
