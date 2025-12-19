import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, d, c = int(input()), dict(), 0
for i in range(n): d[input()] = i
for i in range(n):
    s = input()
    if d[s] > i:
        c += 1
        for k in d.keys():
            if i <= d[k] < d[s]: d[k] += 1
    d[s] = i
print(c)