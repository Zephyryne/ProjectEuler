a = 3
sum = 0
#The maximum value could be 9!*7, which is 2540160, containing seven digits with each being at most 9.
#This begins with a 2, reducing the maximum to 2177282, but this has a second digit of 1, reducing the maximum to 1814403, meaning the first digit must actually be 1, bringing the maximum back up to 1999999.
while a<2000000:
  partial = 0
  for i in range(0,len(str(a))):
    adding = 1
    for j in range(1,(int(str(a)[i])+1)):
      adding = adding * j
    partial+=adding
    if partial>a:
      break
  if partial==a:
    sum+=a
  a+=1
print(sum)