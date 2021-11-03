# 주유소
# 오히려 이건 앞에서부터 접근해야한다.
# 미래의 더 싼 가격의 주유소가 나오기 전까지 구매

N = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

money = 0
dis = 0
min = price[0]
for i in range(N-1):
    if price[i] < min:
        money += dis*min
        dis = 0
        min = price[i]
        
    dis += distance[i]
money += dis*min
print(money)

# distance = [1 for i in range(N-1)]
# price = [1 for i in range(N-1,-1,-1)]

## solution1
# price[-1] = 1000000001
# dis = 0
# money = 0
# for i in range(N-2,-2,-1):
#     if price[i] > price[i+1]:
#         money += price[i+1] * dis
#         dis = 0

#     dis += distance[i]

# print(money)


## solution2
# money = 0
# endIndex = N-1

# while endIndex != 0:
#     minPrice = min(price[0:endIndex])
#     minIndex = price.index(minPrice)
#     # print(minIndex)
#     money += sum(distance[minIndex:endIndex]) * minPrice
#     # print(money)
#     endIndex = minIndex

# print(money)

money = 0
dis = 0
min = price[0]
for i in range(N-1):
    if price[i] < min:
        money += dis*min
        dis = 0
        min = price[i]
        
    dis += distance[i]
money += dis*min
print(money)