import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
data = [[*map(int, input())] for _ in range(n)]


def f(now):
    cnt = [0, 0]
    for i in range(len(now)):
        for j in range(len(now)):
            cnt[now[i][j]] += 1
    
    if cnt[0] and not cnt[1]: print(0, end=''); return
    if not cnt[0] and cnt[1]: print(1, end=''); return

    print('(', end='')

    arr = [[[-1] * (len(now) // 2) for _ in range(len(now) // 2)] for _ in range(4)]
    for i in range(0, len(now) // 2):
        for j in range(0, len(now) // 2):
            arr[0][i][j] = now[i][j]
            arr[1][i][j] = now[i][j + len(now) // 2]
            arr[2][i][j] = now[i + len(now) // 2][j]
            arr[3][i][j] = now[i + len(now) // 2][j + len(now) // 2]

    for nxt in arr: f(nxt)
    print(')', end='')

f(data)