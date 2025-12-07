import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000007

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mat_mul(a, b):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][k] += (a[i][j] * b[j][k]) % MOD
    return res

def fibo(n):
    mat = [[1, 1], [1, 0]]
    res = [[1, 0], [0, 1]]
    while n > 0:
        if n % 2 != 0: res = mat_mul(res, mat)

        mat = mat_mul(mat, mat)
        n //= 2
    return res[0][1] % MOD

n, m = map(int, input().split())
if n == 1 or m == 1:
    print(1)
    exit(0)
if n == m:
    print(fibo(n) % MOD)
    exit(0)

g = gcd(n, m)
print(0 if g == 1 else fibo(g) % MOD)