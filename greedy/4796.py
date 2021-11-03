#캠핑

N=0
ans = []
while True:
    L, P, V = map(int,input().split())
    # 연속하는 P일중 L일만 사용가능

    if (L == 0 and P == 0 and V == 0) or (L>=P or P>=V or L>=V) :
        break
    N +=1
    ans.append((V // P) * L + min(V%P, L))
    # print("Case "+ str(i) + ": " + str(ans))
    # print("Case {}: {}".format(i,ans))


for i in range(N):
    print(f'Case {i+1}: {ans[i]}')
