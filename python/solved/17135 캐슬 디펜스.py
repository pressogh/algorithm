import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from itertools import combinations
from copy import deepcopy

n, m, d = map(int, input().split())
arr = [[*map(int, input().split())] for _ in range(n)]

enemies = []
for i in range(n):
    for j in range(m):
        if arr[i][j]: enemies.append([i, j])


def get_dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def kill(team, a):
    res = [[x[0], x[1], False] for x in a]
    for k in team:
        res.sort(key=lambda x: (get_dist(k, (x[0], x[1])), x[1]))
        if get_dist(k, (res[0][0], res[0][1])) <= d:
            res[0][2] = True
    
    res = [[x[0], x[1]] for x in res if not x[2]]
    return res, len(a) - len(res)


def move(a):
    res = []
    for e in a:
        if e[0] + 1 >= n: continue
        res.append([e[0] + 1, e[1]])
    
    return sorted(res, key=lambda x: x[1])


res = 0
for comb in combinations(range(m), r=3):
    e, cnt = deepcopy(enemies), 0

    team = [(n, c) for c in comb]

    while e:
        ne, c = kill(team, e)
        e, cnt = move(ne), cnt + c

    res = max(res, cnt)

print(res)