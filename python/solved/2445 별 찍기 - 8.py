import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
for i in range(1, n + 1):
    print('*' * i, ' ' * (2 * n - 2 * i), '*' * i, sep='')
for i in range(n - 1, 0, -1):
    print('*' * i, ' ' * (2 * n - 2 * i), '*' * i, sep='')