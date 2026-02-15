import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

n, m, k = map(int, input().split())
n, m = n - 1, m - 1
arr = [[0] * 100 for _ in range(100)]

for i in range(3):
    t = input().split()
    for j in range(3):
        arr[i][j] = int(t[j])
r, c = 3, 3


def calc(x):
    c = Counter(x)
    try:
        c.pop(0)
    except:
        pass

    return [x for p in sorted(c.items(), key=lambda x: (x[1], x[0])) for x in p][:100]


t = 0
while True:
    if arr[n][m] == k: break
    t += 1
    if t > 100: t = -1; break

    if r >= c:
        for i in range(r):
            nxt = calc(arr[i])
            c = max(c, len(nxt))
            for j in range(len(nxt)):
                arr[i][j] = nxt[j]
            for j in range(len(nxt), 100): arr[i][j] = 0
    else:
        for i in range(c):
            nxt = calc([arr[j][i] for j in range(r)])
            r = max(r, len(nxt))
            for j in range(len(nxt)):
                arr[j][i] = nxt[j]
            for j in range(len(nxt), 100): arr[j][i] = 0

print(t)
