import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def f(bombs, n):
    s, e, res = 0, 1, 0
    while e < len(bombs):
        if bombs[e - 1][0] + n < bombs[e][0]:
            res += min(x[1] for x in bombs[s:e])
            s = e
        e += 1
    return res + min(x[1] for x in bombs[s:])

n, bombs = int(input()), sorted([(x, c) for x, c in zip(map(int, input().split()), map(int, input().split()))])
max_cost = int(input())

s, e, res = 0, 2 * (10 ** 8) + 2, 2 ** 31
while s <= e:
    m = (s + e) // 2

    if f(bombs, m) > max_cost: s = m + 1
    else:
        res = min(res, m)
        e = m - 1
print(max(res, 1))
