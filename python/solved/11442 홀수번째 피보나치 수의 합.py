import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000007

def mat_mul(a, b):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][k] += (a[i][j] * b[j][k]) % MOD
    return res

n = int(input())
if n % 2 != 0: n += 1

mat = [[1, 1], [1, 0]]
res = [[1, 0], [0, 1]]
while n > 0:
    if n % 2 != 0: res = mat_mul(res, mat)

    mat = mat_mul(mat, mat)
    n //= 2

print(res[0][1] % MOD)