import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
cols = sorted([[int(x) for x in input().split()] for _ in range(n)])

s, res = [], 0
for col in cols:
    last = None
    while True:
        if not s or s[-1][1] >= col[1]: break
        last = s.pop()

    if last and not s: res += (col[0] - last[0]) * last[1]
    s.append(col)

for i in range(len(s) - 1):
    res += (s[i + 1][0] - s[i][0]) * s[i + 1][1]
print(res + s[0][1])