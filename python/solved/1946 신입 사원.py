import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t:
    t -= 1

    n = int(input())
    sc = [0] * n

    for i in range(n):
        doc, iv = map(int, input().split())
        sc[iv - 1] = doc
    
    res, m = 1, sc[0]
    for i in range(1, n):
        if sc[i] < m:
            m = sc[i]
            res += 1
    print(res)