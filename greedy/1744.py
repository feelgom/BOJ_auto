# 수 묶기
import sys
input = sys.stdin.readline

A = []
B = []
ans = 0

N = int(input())
for i in range(N):
    temp = int(input())
    if temp > 1:
        A.append(temp)
    elif temp ==1:
        ans += 1
    else:
        B.append(temp)

A.sort(reverse=True)
while len(A) >=2:
    ans += A.pop(0) * A.pop(0)

B.sort()
while len(B) >= 2:
    ans += B.pop(0) * B.pop(0)

ans += sum(A) + sum(B)
print(ans)