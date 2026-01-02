import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

fibo = [1, 1, 2]
for i in range(3, 40 + 1): fibo.append(fibo[-1] + fibo[-2])

n, m = int(input()), int(input())
now, res = 0, 1
for _ in range(m):
    vip = int(input()) - 1
    res *= fibo[vip - now]
    now = vip + 1
print(res * fibo[n - now])