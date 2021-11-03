# 뒤집기
# 연속하지 않는 부분이 몇개인지 카운트하고, count/2 가 정답

S = input()
count = 1
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1

print(int(count/2))