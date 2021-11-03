# 카드 정렬하기
# 가장 작은 숫자의 카드 더미 두 개를 비교한다.
# 계속해서 정렬된 상태를 유지하기 위해 heapQueue 를 사용한다.

import sys
import heapq

input = sys.stdin.readline
N= int(input())

cards = []
ans = 0 

for i in range(N):
    heapq.heappush(cards, int(input()))

while len(cards) != 1:
    temp = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards,temp)
    ans += temp

print(ans)









# card = [a]
# i =-1
# sol=[]

# error = 0 
# while True:
#     card.append([])
#     i +=1
#     # Inner while loop begin
#     while len(card[i]) > 0:
#         a = i
#         b = i
        
#         if len(card[i]) >= 2:
#             if len(card[i+1]) == 0:
#                 a=i
#                 b=i
#             elif len(card[i+1]) == 1:
#                 if card[i+1][0] >= card[i][1]:
#                     a =i
#                     b=i
#                 else:
#                     b = i+1
#             else:
#                 temp = card[i][0:2] + card[i+1][0:2]
#                 temp.sort()
#                 if temp[0:2] == card[i][0:2]: 
#                     a= i
#                     b= i    
#                 elif temp[0:2] == card[i+1][0:2]:
#                     a = i+1
#                     b = i+1
#                 else:
#                     b = i+1
#         elif len(card[i]) == 1:
#             if len(card[i+1]) >= 2:
#                 if card[i][0] <= card[i+1][1]:
#                     b = i+1
#                 else:
#                     a = i+1
#                     b= i+1 
#             elif len(card[i+1]) == 1:
#                 b = i+1
#             else: 
#                 print("[Error]1") #len(card[i+1]) == 0:
#                 error = 1
#                 break
#         else: 
#             print("[Error]2 while loop condition ")# len(card[i]) == 0:
     
#         new = card[a][0]+card[b][int(a==b)]
#         card[i+1].append(new)
#         sol.append(new)
#         card[a].pop(0)
#         card[b].pop(0)    
    
#     # Inner while loop end    
    
#     if len(card[i+1]) == 1:
#         print(sum(sol))
#         break

#     if error == 1:
#         break