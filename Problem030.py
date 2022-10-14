#Takes a minute or so to calculate.
sum = 0
for i in range(0,1000000):
  check = 0
  for j in range(0,len(str(i))):
    check += int(str(i)[j])**5
  if check==i:
    sum+=i
print(sum-1) #1^5 is not a solution