# 가장 튼튼한 줄 순서대로 하나씩 갯수를 늘려가면서 더 큰 무게를 들 수 있는지 확인해본다.
# 제출시간 왜이렇게 길게 나오는지 궁금하다...
# sys.stdin.readline 사용하면 시간 줄일 수 있다. - 반복적으로 input()을 받아야 하는 경우 readline 사용!
# 함수 정의하니까 조금 더 줄었다.

import sys
In = sys.stdin.readline

def func():
    N = int(In())
    result = 0
    lines = [int(In()) for i in range(N)]

    lines.sort(reverse=True)

    for i in range(N):
        if lines[i]*(i+1) > result:
            result = lines[i]*(i+1)
    
    print(result)

func()