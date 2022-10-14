irr = "0."

for i in range(1,250001):
    irr += str(i)

ans = int(irr[2])*int(irr[11])*int(irr[101])*int(irr[1001])*int(irr[10001])*int(irr[100001])*int(irr[1000001])
print(ans)
