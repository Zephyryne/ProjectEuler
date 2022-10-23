#Took absolutely forever to calculate
#Edit: See Problem012.cpp for a much faster approach

divs = 0
index = 0
num = 1
while divs<=500:
  divs = 0
  num+=index
  index+=1
  for i in range(1,int(num**0.5)+1):
    if num%i==0:
      divs+=2
print(num)
