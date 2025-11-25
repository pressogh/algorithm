import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
l = []
for _ in range(n):
    start, end = map(int, input().split())
    l.append((start, end))
l.sort(key=lambda x: (x[1], x[0]))

count, end = 1, l[0][1]
for i in range(1, n):
    if l[i][0] >= end:
        end = l[i][1]
        count += 1
print(count)