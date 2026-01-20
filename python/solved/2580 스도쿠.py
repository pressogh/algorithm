import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

SIZE = 9
SQ_SIZE = 3
    

arr = [[*map(int, input().split())] for _ in range(SIZE)]
blank = [(i, j) for i in range(SIZE) for j in range(SIZE) if not arr[i][j]]


def check(y, x, n):
    for i in range(SIZE):
        if arr[y][i] == n or arr[i][x] == n: return False

    for i in range(SQ_SIZE):
        for j in range(SQ_SIZE):
            if arr[y // SQ_SIZE * SQ_SIZE + i][x // SQ_SIZE * SQ_SIZE + j] == n: return False
    
    return True


def dfs(n):
    if n == len(blank):
        for a in arr: print(*a)
        exit(0)
    
    y, x = blank[n]
    for v in range(1, 10):
        if not check(y, x, v): continue
        arr[y][x] = v
        dfs(n + 1)
        arr[y][x] = 0


dfs(0)