import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from copy import deepcopy

def mat_mul(n, a, b):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][k] += a[i][j] * b[j][k] % 1000
    return res

n, b = map(int, input().split())
a = [[int(x) for x in input().split()] for _ in range(n)]

b -= 1
mat = deepcopy(a)
while b > 0:
    if b % 2 != 0: mat = mat_mul(n, mat, a)
    
    a = mat_mul(n, a, a)
    b //= 2

for item in mat:
    print(*[x % 1000 for x in item])