final = []

for a in range(2,101):
    for b in range(2,101):
        num = a**b
        if num not in final:
            final.append(num)

print(len(final))
