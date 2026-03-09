import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
arr = [int(input()) for _ in range(n)]
arr.reverse()

s, res = [0], [0] * n
for i in range(1, n):
    while True:
        if not s or arr[s[-1]] >= arr[i]: break

        now = s.pop()
        res[i] += res[now] + 1
    s.append(i)

print(sum(res))