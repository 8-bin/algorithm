S = list(input())
for i in range(len(S)):
    print(S[i], end='')
    if (i+1) % 10 == 0:
        print()