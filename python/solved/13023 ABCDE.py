import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
connect = [[] for _ in range(n)]

while m:
    m -= 1
    a, b = map(int, input().split())

    connect[a].append(b)
    connect[b].append(a)


def f(now, depth):
    if depth >= 4:
        print(1)
        exit(0)

    for conn in connect[now]:
        if v[conn]: continue

        v[conn] = True
        f(conn, depth + 1)
        v[conn] = False


v = [False] * n
for i in range(n):
    v[i] = True
    f(i, 0)
    v[i] = False

print(0)