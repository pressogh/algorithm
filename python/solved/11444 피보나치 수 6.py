import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000007

def mat_mul(n, a, b):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][k] += (a[i][j] * b[j][k]) % MOD
    return res

n = int(input())
if n == 0:
    print(0)
    exit(0)

mat = [[1, 1], [1, 0]]
res = [[1, 1], [1, 0]]
n -= 1
while n > 0:
    if n % 2 != 0: res = mat_mul(2, res, mat)

    mat = mat_mul(2, mat, mat)
    n //= 2

print(res[0][1] % MOD)
