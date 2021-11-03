# 더하기 연산을 먼저 한 뒤에 빼기 연산을 하자

input = input().split('-')

count = 0
for cell in input:
    cal = list(map(int,cell.split('+')))
    if count == 0:
        result = sum(cal)
    else:
        result -= sum(cal)
    count +=1

print(result)