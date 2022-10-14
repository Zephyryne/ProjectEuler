total = 0

for i in range(1,1000001):
    if str(i) == str(i)[::-1]:
        if bin(i)[2:] == str(bin(i)[2:])[::-1]:
            total += i

print(total)

#ez clap, totally no cheats
