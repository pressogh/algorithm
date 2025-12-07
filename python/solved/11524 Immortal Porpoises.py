import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 1000000000

def mat_mul(a, b):
    res = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][k] += (a[i][j] * b[j][k]) % MOD
    return res

t = int(input())
while t > 0:
    t -= 1

    k, y = map(int, input().split())
    y -= 1

    mat = [[1, 1], [1, 0]]
    res = [[1, 1], [1, 0]]
    while y > 0:
        if y % 2 != 0: res = mat_mul(res, mat)

        mat = mat_mul(mat, mat)
        y //= 2
    
    print(k, res[0][1] % MOD)