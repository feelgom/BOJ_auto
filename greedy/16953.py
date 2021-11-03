import heapq
A,B = map(int, input().split())
# print(B)

flag = True
sol = [(A,1)]
# print(sol)
while True:
    if len(sol) == 0:
        flag = False
        break

    temp = sol[-1]
    sol.remove(temp)
    if temp[0] == B:
        break
    if temp[0] * 2 <= B:
        sol.append( (temp[0] * 2, temp[1]+1) ) 
    if temp[0] * 10 + 1 <= B:
        sol.append( (temp[0] * 10 + 1, temp[1]+1) )
    
    # print(sol)

if flag:
    print(temp[1])
else:
    print(-1)


# while A < B:
#     if B%10 == 1:
#         B = B//10
#         count += 1
#         # print(B)
#         continue

#     if B%2 ==0:
#         B = B//2
#         # print(B)
#         count += 1
#         continue

# if A == B:
#     print(count+1)
# elif A>B:
#     print(-1)


