def checkgroup(word):
    memo = []
    current = ''
    count = len(word)
    for i in word:
        if i not in memo or (i == current):
            current = i
            memo.append(i)
            count -= 1
        else:
            return 0
    if count == 0:
        return 1
 
N = int(input())
result = 0
for _ in range(N):
    word = input()
    result += checkgroup(word)

print(result)  