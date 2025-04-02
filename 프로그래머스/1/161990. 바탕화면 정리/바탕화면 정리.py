def solution(wallpaper):
    lux = float('inf') # 최소값을 구하기 위해 
    luy = float('inf')
    rdx = -1 # 최대값을 구하기 위해 
    rdy = -1

    # wallpaper 순회
    for i in range(len(wallpaper)):       # 행 인덱스 (x)
        for j in range(len(wallpaper[i])): # 열 인덱스 (y)
            if wallpaper[i][j] == '#':
                # 가장 위, 왼쪽은 최소값
                lux = min(lux, i)
                luy = min(luy, j)
                # 가장 아래, 오른쪽은 최대값 + 1
                rdx = max(rdx, i + 1)
                rdy = max(rdy, j + 1)

    return [lux, luy, rdx, rdy]