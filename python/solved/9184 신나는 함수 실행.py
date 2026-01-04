import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dp = dict()
dp[(0, 0, 0)] = 1
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: a, b, c = 0, 0, 0
    if a > 20 or b > 20 or c > 20: a, b, c = 20, 20, 20
    if (a, b, c) in dp: return dp[(a, b, c)]
    
    if a <= 0 or b <= 0 or c <= 0: return 1
    if a > 20 or b > 20 or c > 20: return w(20, 20, 20)
    if a < b < c:
        dp[(a, b, c)] = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
        return dp[(a, b, c)]
    
    dp[(a, b, c)] = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    return dp[(a, b, c)]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1: break

    print(f"w({a}, {b}, {c}) = {w(a, b, c)}")