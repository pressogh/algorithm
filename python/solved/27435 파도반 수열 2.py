import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 998244353

def mat_mul(a, b):
    res = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                res[i][k] += (a[i][j] * b[j][k]) % MOD
    return res

def f(n):
    mat = [[0, 1, 1], [1, 0, 0], [0, 1, 0]]
    res = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    while n > 0:
        if n % 2 != 0: res = mat_mul(res, mat)

        mat = mat_mul(mat, mat)
        n //= 2
    return res[0][1] % MOD

t = int(input())
while t > 0:
    t -= 1

    n = int(input())
    print(f(n))