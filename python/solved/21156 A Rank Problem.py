import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
rank = [f"T{i}" for i in range(1, n + 1)]

while m > 0:
    m -= 1
    e, s = input().split()
    e, s = rank.index(e), rank.index(s)

    while s < e:
        t = rank[s]
        rank[s] = rank[s + 1]
        rank[s + 1] = t
        s += 1
print(*rank)