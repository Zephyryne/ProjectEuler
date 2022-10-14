max = 0
#1thru5 digits are optimal
for i in range(1,99999):
  check = ""
  j = 1
  while len(check) <= 9:
    if len(check)==9 and int(check) > max:
      if "1" in check and "2" in check and "3" in check and "4" in check and "5" in check and "6" in check and "7" in check and "8" in check and "9" in check:
        max = int(check)

    check += str(i*j)
    j += 1
    
print(max)

#did print(check) and made a mess, oops