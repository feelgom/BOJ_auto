# 신입 사원
import sys
In = sys.stdin.readline
# In = input
T = int(In())
for _ in range(T):
    N = int(In())
    candidate = dict([list(map(int,In().split())) for i in range(N)])
    
    th = 100000
    count = 0
    for i in range(1,N+1):
        if candidate[i] <= th:
            th = candidate[i]
            count += 1
            if th == 1:
                break
    
    print(count)
