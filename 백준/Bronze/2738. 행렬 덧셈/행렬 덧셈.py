N, M = map(int, input().split())
new_arr = [[0] * M for _ in range(N)]
arr1 = []
arr2 = []

for _ in range(N):
    arr1.append(list(map(int, input().split())))

for _ in range(N):
    arr2.append(list(map(int, input().split())))
    
for i in range(N):
    for j in range(M):
        new_arr[i][j] = arr1[i][j] + arr2[i][j]
        
for i in range(N):
    for j in range(M):
        print(new_arr[i][j], end=' ')
    print()