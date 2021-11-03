import sys
In = sys.stdin.readline
# In= input

N = int(In())
letters = [In().strip() for i in range(N)]

val = [0 for i in range(26)]
ans =0
for letter in letters:
    leng = len(letter)
    for i in range(len(letter)):
        val[ord(letter[i])-ord('A')] += 10**(leng-1-i)

val.sort(reverse=True)
for i in range(9):
    ans += val[i]*(9-i)

print(ans)