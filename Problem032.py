valid = []
sum = 0
#two cases: 1&4 digits or 2&3 digits
for i in range(1,10):
  for j in range(1000,10000):
    check = str(i) + str(j) + str(i*j)
    if len(check) == 9:
      if str(i*j) not in valid:
        if "1" in check and "2" in check and "3" in check and "4" in check and "5" in check and "6" in check and "7" in check and "8" in check and "9" in check:
          valid.append(str(i*j))
          sum += i*j
for i in range(10,100):
  for j in range(100,1000):
    check = str(i) + str(j) + str(i*j)
    if len(check) == 9:
      if str(i*j) not in valid:
        if "1" in check and "2" in check and "3" in check and "4" in check and "5" in check and "6" in check and "7" in check and "8" in check and "9" in check:
          valid.append(str(i*j))
          sum += i*j
print(sum)