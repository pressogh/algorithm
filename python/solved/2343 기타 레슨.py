import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def f(lec, n):
    res, c = 0, 0
    for i in range(len(lec)):
        if c + lec[i] > n:
            res += 1
            c = 0
        c += lec[i]
    return res

n, m = map(int, input().split())
lectures = [int(x) for x in input().split()]

s, e = 0, 1 << 32
while s <= e:
    mid = (s + e) // 2
    
    if f(lectures, mid) < m: e = mid - 1
    else: s = mid + 1
print(max(s, max(lectures)))