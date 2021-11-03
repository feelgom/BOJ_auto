#수들의 합
N = int(input())

ans = 0
i=0
while ans <= N:
    i+=1
    ans = i*(i+1)/2

print(ans)
print(i-1)

# print(   int(  ( ( int(input()) * 8 + 1  )**.5-1 ) / 2    ) )