# 보석도둑
# sol1) 작은 가방부터 담을수 있는 보석 중 제일 비싼 보석을 담으면 된다.
# -> 이중 for loop 때문에 시간초과
# sol2) 보석 value 기준 내림차순 정렬후 담을 수 있는거 담기
# 이중 for문 정렬 https://haesoo9410.tistory.com/193

import sys
import heapq
input = sys.stdin.readline

N, K = map(int,input().split())
jewels = [list(map(int,input().split())) for i in range(N)]
bags = [int(input()) for i in range(K)]
jewels.sort(key = lambda x:x[0])
bags.sort()

maxheap= []
ans = 0

idx = 0
for i in range(K):
    while idx < N and bags[i] >= jewels[idx][0]:
        heapq.heappush(maxheap, (-jewels[idx][1],jewels[idx][1]))
        idx += 1
    if len(maxheap) != 0:
        ans += heapq.heappop(maxheap)[1]
    


# for jewel in jewels:
#     if jewel[0] <= bags[-1]:
#         for bag in bags:
#             if jewel[0] <= bag:
#                 ans += jewel[1]
#                 bags.remove(bag)  
#                 break
#     if len(bags) == 0:
#         break

print(ans)
