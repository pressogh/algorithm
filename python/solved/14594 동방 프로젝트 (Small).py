import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = int(input()), int(input())
l = [[i] for i in range(1, n + 1)]

b = sorted([[int(x) for x in input().split()] for _ in range(m)])
t = []

for item in b:
    if not t:
        t.append(item)
        continue

    if t[-1][0] <= item[0] <= t[-1][1]: t[-1] = [min(t[-1][0], item[0]), max(t[-1][1], item[1])]
    else: t.append(item)

t = [[0, 0]] + t + [[n + 1, n + 1]]
res = len(t) - 2
for i in range(len(t) - 1):
    res += t[i + 1][0] - t[i][1] - 1
print(res)
