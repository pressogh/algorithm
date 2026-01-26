import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
sky = [[-1] * m for _ in range(n)]
for i in range(n):
    now = input()
    for j in range(m):
        if now[j] == 'c':
            sky[i][j] = 0

while True:
    flag = False
    for i in range(n):
        for j in range(m - 1, 0, -1):
            if sky[i][j] == -1 and sky[i][j - 1] != -1:
                sky[i][j] = sky[i][j - 1] + 1
                flag = True
    if not flag: break

for s in sky: print(*s)
