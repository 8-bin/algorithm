N = int(input())

for i in range(1, N+1):
    print(' ' * (N-i), end='')
    for j in range(1, 2 * i):
        if i == N:
            print('*', end='')
        else:
            if j == 1 or j == (2*i-1):
                print('*', end='')
            else:
                print(' ', end='')
    print()