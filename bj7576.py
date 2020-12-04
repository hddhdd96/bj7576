import sys
from collections import deque

X, Y = map(int, sys.stdin.readline().split())
box = []
loc = deque()
for i in range(Y):
    row = list(map(int, sys.stdin.readline().split()))
    for j in range(X):
        if row[j] == 1:
            loc.append([i, j])
    box.append(row)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
cnt = 1
while loc:
    y, x = loc.popleft()

    for l in range(4):
        move_x = x + dx[l]
        move_y = y + dy[l]

        if move_x < 0 or move_y < 0 or move_x >= X or move_y >= Y or box[move_y][move_x] == -1:
            continue

        if box[move_y][move_x] == 0:
            box[move_y][move_x] = box[y][x] + 1
            loc.append([move_y, move_x])
            cnt = box[move_y][move_x]

hoxy = True
for k in box:
    if 0 in k:
        print(-1)
        hoxy = False
        break

if hoxy == True:
    if cnt == 1:
        print(0)
    elif cnt != 1:
        print(cnt - 1)
