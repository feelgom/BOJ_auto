N = int(input())

time = []
for i in range(N):
    time.append(list(map(int,input().split())))

count = 1
time.sort()
start = time[-1][0]
for i in range(N-2,-1,-1):
    if time[i][1] <= start:
        count +=1
        start = time[i][0]

print(count)
        
    