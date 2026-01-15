import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000007

n, m = map(int, input().split())
if n < m: print(1); exit(0)
if n == m: print(2); exit(0)


def mat_mul(a, b):
    res = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            for k in range(m):
                res[i][k] = (res[i][k] + a[i][j] * b[j][k]) % MOD
    return res


mat = [[0] * m for _ in range(m)]
mat[0][0], mat[0][-1] = 1, 1
for i in range(1, m): mat[i][i - 1] = 1

res = [[int(i == j) for j in range(m)] for i in range(m)]
while n > 0:
    if n % 2: res = mat_mul(res, mat)

    mat = mat_mul(mat, mat)
    n //= 2

print(res[0][0] % MOD)
