T = int(input())
for _ in range(T):
    N = int(input())
    price = list(map(int,input().split()))
    earn = 0
    max = 0
    for i in range(N-1,-1,-1):
        if price[i] > max:
            max = price[i]
        else:
            earn += max-price[i]
    print(earn)

