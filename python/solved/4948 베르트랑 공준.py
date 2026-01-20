import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

prime = [True] * (123456 * 2 + 1)
for i in range(2, int((123456 * 2 + 1) ** 0.5) + 1):
    if not prime[i]: continue
    for j in range(i * 2, 123456 * 2 + 1, i):
        prime[j] = False

while True:
    n = int(input())
    if n == 0: break

    res = 0
    for i in range(n + 1, 2 * n + 1): res += int(prime[i])
    print(res)