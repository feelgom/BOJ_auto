# 설탕 배달
# https://www.acmicpc.net/problem/2839
# https://www.acmicpc.net/submit/2839

N = int(input())

a,b = 0,0
sum = 0
end = 0
while sum <= N:
    a+=1
    sum = 5*a + 3*b
    if sum ==N:
        print(a+b)
        end =1

while a > 0 and end ==0:
    a -=1
    sum = 5*a + 3*b
    while sum <= N and end ==0:
        b+=1
        sum = 5*a +3*b
        if sum == N:
            print(a+b)
            end = 1

if end ==0:
    print(-1)
