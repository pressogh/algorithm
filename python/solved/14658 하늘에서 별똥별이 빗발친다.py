import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m, l, k = map(int, input().split())
meteors = [[int(x) for x in input().split()] for _ in range(k)]

res = k
for i in range(k):
    for j in range(k):
        x, y, c = meteors[i][0], meteors[j][1], 0
        for meteor in meteors:
            if x <= meteor[0] <= x + l and y <= meteor[1] <= y + l: c += 1
        res = min(res, k - c)

print(res)