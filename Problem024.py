# 1 2 3 4 5 6 7 8 9 10
# a b c d e f g h i  j


nums = []
for a in range(0,3):
    for b in range(0,10):
        if a == b:
            continue
        else:
            for c in range(0,10):
                if c in [a,b]:
                    continue
                else:
                    for d in range(0,10):
                        if d in [a,b,c]:
                            continue
                        else:
                            for e in range(0,10):
                                if e in [a,b,c,d]:
                                    continue
                                else:
                                    for f in range(0,10):
                                        if f in [a,b,c,d,e]:
                                            continue
                                        else:
                                            for g in range(0,10):
                                                if g in [a,b,c,d,e,f]:
                                                    continue
                                                else:
                                                    for h in range(0,10):
                                                        if h in [a,b,c,d,e,f,g]:
                                                            continue
                                                        else:
                                                            for i in range(0,10):
                                                                if i in [a,b,c,d,e,f,g,h]:
                                                                    continue
                                                                else:
                                                                    for j in range(0,10):
                                                                        if j in [a,b,c,d,e,f,g,h,i]:
                                                                            continue
                                                                        else:
                                                                            adding = str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g)+str(h)+str(i)+str(j)
                                                                            nums.append(adding)
                                        

nums.sort()
print(nums[999999])
