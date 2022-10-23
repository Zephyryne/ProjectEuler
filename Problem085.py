maxbelow = 0
maxabove = 1249537809128347

a = 1
while a < 100:
    for b in range(1,a+1):
        rects = a*(a+1)*b*(b+1)/4
        if rects < 2000000 and rects > maxbelow:
            maxbelow = rects
            areabelow = a*b
        elif rects > 2000000 and rects < maxabove:
            maxabove = rects
            areaabove = a*b
    a += 1

if (2000000-maxbelow) < (maxabove-2000000):
    print(areabelow)
else:
    print(areaabove)
