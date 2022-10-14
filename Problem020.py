factorial = 1
for i in range(1,101):
  factorial = factorial * i
factorial = str(factorial)
sum = 0
for i in range(0,(len(factorial))):
  sum+=int(factorial[i])
print(sum)