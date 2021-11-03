T = int(input())

buttons = [300, 60, 10]
count = [0, 0, 0]
for i in range(3):
    count[i] = T//buttons[i]
    T = T%buttons[i]
    if T == 0:
        break

if T != 0:
    print(-1)

else:
    print(*count)


# n=int(input())
# a=n//300
# b=n%300//60
# c=n%60//10
# print(*[[-1],[n//300,n//60%5,n//10%6]][n//10==n/10])



