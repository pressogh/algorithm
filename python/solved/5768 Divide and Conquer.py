import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def calc(n):
    t = [0] * (5000 + 1)
    now = 2
    while n > 1:
        if n % now == 0:
            t[now] += 1
            n //= now
        else: now += 1
    
    res = 1
    for x in t:
        if x != 0: res *= (x + 1)
    return res

res = [0, 0]
while True:
    n, m = map(int, input().split())
    if n == m == 0: break

    for i in range(n, m + 1):
        t = calc(i)
        if t >= res[1]:
            res[0], res[1] = i, t
    print(*res)