import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

CYCLE = 15 * (100_000)

memo = [0, 1, 1]
for _ in range(3, CYCLE):
    memo.append((memo[-2] + memo[-1]) % 1000000)

n = int(input())
print(memo[n % len(memo)])
