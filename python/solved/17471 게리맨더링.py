import sys
input = sys.stdin.readline

n = int(input())
arr = [*map(int, input().split())]

connect = [[] for _ in range(n)]
for i in range(n):
    c = list(map(int, input().split()))
    for v in c[1:]:
        connect[i].append(v - 1)


def check(group):
    start = next(iter(group))
    s, visited = [start], {start}

    res = arr[start]
    while s:
        now = s.pop()

        for nxt in connect[now]:
            if nxt in group and nxt not in visited:
                visited.add(nxt)
                s.append(nxt)
                res += arr[nxt]

    if len(visited) != len(group): return -1
    return res


res = 1 << 31
for mask in range(1, 1 << n):
    if not (mask & 1): continue

    r, b = set(), set()
    for i in range(n):
        if mask & (1 << i): r.add(i)
        else: b.add(i)

    if not r or not b: continue

    r_sum = check(r)
    if r_sum == -1: continue

    b_sum = check(b)
    if b_sum == -1: continue

    res = min(res, abs(r_sum - b_sum))


print(res if res != (1 << 31) else -1)
