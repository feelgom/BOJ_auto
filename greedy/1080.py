import sys
# input = sys.stdin.readline

n,m = map(int, input().split())

# a = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
a= [ list(input().rstrip()) for i in range(n)]
b= [ list(input().rstrip()) for i in range(n)]

def flip(x,y):
    for i in range(x,x+3):
        for j in range(y,y+3):
            if a[i][j] == '1':
                a[i][j] = '0'
            else:
                a[i][j] = '1'

flag = True
count = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            flip(i,j)
            count += 1

for i in range(n):
    if a[i] != b[i]:
        flag = False

if flag == True:
    print(count)
else:
    print(-1)