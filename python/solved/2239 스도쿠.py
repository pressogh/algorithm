import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

board = [[*map(int, list(input()))] for _ in range(9)]
blank = []
for i in range(9):
    for j in range(9):
        if not board[i][j]: blank.append((i, j))


def check(y, x, n):
    for i in range(9):
        if board[y][i] == n or board[i][x] == n: return False
    for i in range(y // 3 * 3, (y // 3 + 1) * 3):
        for j in range(x // 3 * 3, (x // 3 + 1) * 3):
            if n == board[i][j]: return False
    return True

def f(n):
    if n == len(blank):
        for b in board: print(*b, sep='')
        exit(0)

    y, x = blank[n]
    for i in range(1, 10):
        if not check(y, x, i): continue
        board[y][x] = i
        f(n + 1)
        board[y][x] = 0

print(f(0))