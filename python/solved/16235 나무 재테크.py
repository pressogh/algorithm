import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

dy, dx = [0, 1, 0, -1, 1, 1, -1, -1], [1, 0, -1, 0, 1, -1, 1, -1]

n, m, k = map(int, input().split())

arr = [[*map(int, input().split())] for _ in range(n)]
ground = [[5] * n for _ in range(n)]

trees = [[deque() for _ in range(n)] for _ in range(n)]
while m:
    m -= 1
    y, x, age = map(int, input().split())

    trees[y - 1][x - 1].append(age)

while k:
    k -= 1
    
    for i in range(n):
        for j in range(n):
            if not trees[i][j]: continue
                
            target_idx = -1
            for t in range(len(trees[i][j])):
                if ground[i][j] < trees[i][j][t]:
                    target_idx = t
                    break
                ground[i][j] -= trees[i][j][t]
                trees[i][j][t] += 1

            if target_idx == -1: continue

            dead_trees = trees[i][j]
            for _ in range(len(dead_trees) - target_idx):
                ground[i][j] += dead_trees.pop() // 2

    # 가을
    for i in range(n):
        for j in range(n):
            for t in range(len(trees[i][j])):
                if trees[i][j][t] % 5: continue

                for d in range(8):
                    ny, nx = i + dy[d], j + dx[d]
                    if 0 <= ny < n and 0 <= nx < n:
                        trees[ny][nx].appendleft(1)
    
    # 겨울
    for i in range(n):
        for j in range(n):
            ground[i][j] += arr[i][j]


res = 0
for i in range(n):
    for j in range(n):
        res += len(trees[i][j])

print(res)