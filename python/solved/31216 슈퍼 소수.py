import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

check = [True] * (318137 + 1)
check[0], check[1] = False, False
prime = []
for i in range(2, 318137 + 1):
    if not check[i]: continue
    prime.append(i)
    for j in range(i * 2, 318137 + 1, i):
        check[j] = False

super_prime = []
for i in range(len(prime)):
    now = i + 1
    if check[now]:
        super_prime.append(prime[i])

t = int(input())
while t:
    t -= 1

    n = int(input())
    print(super_prime[n - 1])
