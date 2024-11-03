from collections import deque

M,N = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
tomato = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            tomato.append((i,j)) # 값이 1인 [x,y] 좌표

dx = [0,0,-1,1]
dy = [1,-1,0,0]
d_day = 0

while tomato:
    for _ in range(len(tomato)):
        x,y = tomato.popleft()
        for d in range(4):
            nx = x+dx[d]
            ny = y+dy[d]
            if 0<= nx < N and 0<= ny < M:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 1
                    tomato.append((nx,ny))
    if tomato:
        d_day += 1

for r in arr:
    if 0 in r:
        print(-1)
        break
else:
    print(d_day)
