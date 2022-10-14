def d(n):
  sum = 0
  for i in range(1,int(n**0.5)):
    if n%i == 0:
      if i == 1:
        sum += 1
      elif n == i**2:
        sum += i
      else:
        sum += (i + (n/i))
  return sum
answer = 0
for a in range(1,10000):
  if d(d(a)) == a and d(a) != a:
    answer += a
print(answer)