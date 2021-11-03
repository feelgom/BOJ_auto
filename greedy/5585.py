N = 1000 - int(input())
coins = [500,100,50,10,5,1]

count = 0
for coin in coins:
    count+= N//coin
    N = N%coin
    if N == 0:
        break
print(count)
