import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

fibo = [0] * 3
fibo[0], fibo[1], fibo[2] = 1, 1, 2
for i in range(4, n + 1):
    fibo[0], fibo[1] = fibo[1], fibo[2]
    fibo[2] = (fibo[0] + fibo[1]) % 1000000007

print(fibo[-1] % 1000000007, (n - 3 + 1) % 1000000007)