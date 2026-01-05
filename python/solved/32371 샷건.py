import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [0, 0, 1, 0, -1, 1, -1, 1, -1], [0, 1, 0, -1, 0, -1, 1, 1, -1]

keyboard = [input() for _ in range(4)]
memo = input()
for i in range(1, 9):
    for j in range(1, 9):
        flag = True
        for k in range(9):
            ny, nx = i + dy[k], j + dx[k]
            if keyboard[ny][nx] not in memo: flag = False; break
        if flag: print(keyboard[i][j]); exit(0)
