from math import log

ans = 0
check = 0
bases = []
expos = []

with open("p099_base_exp.txt") as f:
    for line in f:
        a,b = map(int, line.split(","))
        bases.append(a)
        expos.append(b)

for i in range(0,1000):
    if expos[i]*log(bases[i]) > check:
        ans = i + 1 #because expos[0] is on line 1
        check = expos[i]*log(bases[i])

print(ans)
