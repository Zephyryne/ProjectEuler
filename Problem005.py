max = 2*3*4*5*6*7*8*9*10*11*12*13*14*15*16*17*18*19*20
primes = 2*3*5*7*11*13*17*19
for i in range(20,max):
  done = True
  for j in range(2,21):
    if (primes*i)%j!=0:
      done = False
      break
  if done==True:
    print(primes*i)
    break