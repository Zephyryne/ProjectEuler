#Took several minutes to calculate
num = 4
maxlen = 0
max = 0
while num<1000000:
  chain = 1
  test = num
  while test!=1:
    if test%2==0:
      test/=2
    else:
      test=(3*test)+1
    chain+=1
  if chain>maxlen:
    maxlen = chain
    max = num
  num+=1
print(max)