from math import gcd

nums = [2,1]
k = 1
for i in range(33):
    nums.append(2*k)
    nums.append(1)
    nums.append(1)
    k += 1

num = 1
den = 1
store_num = 1

for j in range(99):
    place = 98 - j
    num, den = int((nums[place] * num) + den), num
    #store_num = int(num)
    #num = int((nums[place] * num) + den)
    #den = store_num
    #reduce = gcd(num, den)
    #num /= reduce
    #den /= reduce

ans = 0
num = int(num)
for digit in str(num):
    ans += int(digit)
print(num)
print(ans)

#Reducing gives the wrong answer wtf
