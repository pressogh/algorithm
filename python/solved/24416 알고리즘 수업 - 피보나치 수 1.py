import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())

f_cnt = 0
fibo = [0] * (n + 1)
fibo[1], fibo[2] = 1, 1
for i in range(3, n + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(fibo[-1], n - 3 + 1)