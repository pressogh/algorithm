import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(n)]

m, k = map(int, input().split())
b = [[int(x) for x in input().split()] for _ in range(m)]

met = [[0] * k for _ in range(n)]
for i in range(n):
    for j in range(m):
        for l in range(k):
            met[i][l] += a[i][j] * b[j][l]

for item in met:
    print(*item)