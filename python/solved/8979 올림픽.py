import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())
l = []
for _ in range(n):
    medal = [int(x) for x in input().split()]
    l.append((-medal[1], -medal[2], -medal[3], medal[0]))
l.sort()

s = 0
for i in range(0, n):
    if l[i][3] == k:
        res = i + 1
        for j in range(i - 1, -1, -1):
            if not (l[i][0] == l[j][0] and l[i][1] == l[j][1] and l[i][2] == l[j][2]): break
            res -= 1
        print(res)
        break