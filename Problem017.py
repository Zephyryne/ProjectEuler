sum = 0
for j in range(1,1001):
  i = j
  if len(str(i))==4:
    sum+=11 #oneth-ousan-d
    break
  if i%100==0:
    #one,two,three,four,five,six,seven,eight,nine
    if int(str(i)[0]) in [1,2,6]:
      sum+=10 #onehu-ndred
    elif int(str(i)[0]) in [4,5,9]:
      sum+=11
    elif int(str(i)[0]) in [3,7,8]:
      sum+=12
  if len(str(i))==3 and i%100!=0:
    if int(str(i)[0]) in [1,2,6]:
      sum+=13 #onehu-ndred-and
    elif int(str(i)[0]) in [4,5,9]:
      sum+=14
    elif int(str(i)[0]) in [3,7,8]:
      sum+=15
    i = int(str(i)[1:])
  if len(str(i))==2:
    #ten(special), twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
    if int(str(i)[0]) in [4,5,6]:
      sum+=5
    elif int(str(i)[0]) in [2,3,8,9]:
      sum+=6
    elif int(str(i)[0])==7:
      sum+=7
    elif int(str(i)[0])==1:
      #ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
      if int(str(i)[1])==0:
        sum+=3
      elif int(str(i)[1]) in [1,2]:
        sum+=6
      elif int(str(i)[1]) in [5,6]:
        sum+=7
      elif int(str(i)[1]) in [3,4,8,9]:
        sum+=8
      elif int(str(i)[1])==7:
        sum+=9
    if int(str(i)[0])!=1:
      i = int(str(i)[1:])
    else:
      i = 0
  if len(str(i))==1 and i!=0:
    if int(str(i)[0]) in [1,2,6]:
      sum+=3 #one
    elif int(str(i)[0]) in [4,5,9]:
      sum+=4
    elif int(str(i)[0]) in [3,7,8]:
      sum+=5
print(sum)