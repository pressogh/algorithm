import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

# https://kkigon.tistory.com/36
def f(n):
    n, res, size = n + 1, 0, 1
    while size < n:
        size <<= 1
    
    while size > 1:
        res += (n // size) * (size // 2)
        if n // (size // 2) % 2 != 0: res += n % (size // 2)
        size //= 2
    return res

a, b = map(int, input().split())
print(f(b) - f(a - 1))
