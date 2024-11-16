N = int(input())

for i in range(1, N+1):
    print(' ' * (N - i), end='')
    for j in range(1, 2 * i):
        if j % 2 == 0:
            print(" ", end='')
        elif j % 2 == 1:
            print("*", end='')
    print()