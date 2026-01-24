import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
room = [['X'] * (n + 2)] + [['X'] + list(input()) + ['X'] for _ in range(n)] + [['X'] * (n + 2)]

v, h = 0, 0
for i in range(n + 1):
    for j in range(n + 1):
        if room[i][j] == 'X':
            if j < n and room[i][j + 1] == room[i][j + 2] == '.': v += 1
            if i < n and room[i + 1][j] == room[i + 2][j] == '.': h += 1
print(v, h)