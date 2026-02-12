import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import defaultdict

n = int(input())
arr = [list(input()) for _ in range(n)]


def count():
    res = 0
    for i in range(n):
        j, last, c = 0, arr[i][0], 0
        while j < n:
            c += 1
            if last != arr[i][j]:
                c = 0
                last = arr[i][j]
                continue
            else: res = max(res, c)
            j += 1
        
        j, last, c = 0, arr[0][i], 0
        while j < n:
            c += 1
            if last != arr[j][i]:
                c = 0
                last = arr[j][i]
                continue
            else: res = max(res, c)
            j += 1
    
    return res


res = 0
for i in range(n):
    for j in range(n):
        if i != n - 1 and arr[i][j] != arr[i + 1][j]:
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]
            res = max(res, count())
            arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

        if j != n - 1 and arr[i][j] != arr[i][j + 1]:
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]
            res = max(res, count())
            arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

print(res)