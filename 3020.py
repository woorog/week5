import sys
from itertools import count

n,h=map(int,sys.stdin.readline().split())

up = [0] * (h + 1)  # 위에서 내려오는 벽돌
down = [0] * (h + 1)  # 아래에서 올라가는 벽돌
for i in range(n):
    block = int(sys.stdin.readline())
    if i % 2 == 0:  # 짝수 인덱스, 아래에서 올라감
        down[block] += 1
    else:  # 홀수 인덱스, 위에서 내려옴
        up[h - block + 1] += 1
# 누적 합 계산
for i in range(h - 2, -1, -1):
    down[i] += down[i + 1]
for i in range(1, h):
    up[i] += up[i - 1]

# 각 높이에서의 장애물의 총 개수 계산
obstacles = [down[i] + up[i] for i in range(h)]

# 최소 장애물 개수와 그 개수 찾기
min_obstacles = min(obstacles)
count = obstacles.count(min_obstacles)

print(min_obstacles, count)