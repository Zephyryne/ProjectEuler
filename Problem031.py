coins = [1, 2, 5, 10, 20, 50, 100, 200]
count = [1] + [0] * 200
#one way to get 0p

for a in coins:
    for i in range(a, 201):
        count[i] += count[i - a]
        #say you want 40p with 1 20p coin:
        #just look at how many ways you can get 20p otherwise

print(count[200])
