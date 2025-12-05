# 피사노 수열 사용
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

CYCLE = 15 * (10 ** 3)

memo = [0, 1, 1]
for _ in range(3, CYCLE):
    memo.append((memo[-2] + memo[-1]) % 10000)

while True:
    n = int(input())
    if n == -1: break
    
    print(memo[n % CYCLE] % 10000)

# 행렬곱 + 분할 정복을 이용한 거듭제곱 사용
"""
import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

MOD = 10000

def mat_mul(n, a, b):
    res = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                res[i][k] += (a[i][j] * b[j][k]) % MOD
    return res

while True:
    n = int(input())
    if n == -1: break
    if n == 0:
        print(0)
        continue
    
    mat = [[1, 1], [1, 0]]
    res = [[1, 1], [1, 0]]
    n -= 1
    while n > 0:
        if n % 2 != 0: res = mat_mul(2, res, mat)

        mat = mat_mul(2, mat, mat)
        n //= 2
    
    print(res[0][1] % MOD)
"""