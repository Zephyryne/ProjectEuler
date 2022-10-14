def is_Lychrel(x):
  for i in range(0,50):
    x += int(str(x)[::-1])
    if x == int(str(x)[::-1]):
      return False
  return True

answer = 0
for num in range(0,10000):
  if is_Lychrel(num) == True:
    answer += 1
print(answer)