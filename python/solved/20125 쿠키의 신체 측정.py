import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
l = [input() for _ in range(n)]

hart = None

now = 0
while True:
    for i in range(n):
        if l[now][i] == '*':
            hart = [now + 1, i]
            break
    now += 1
    if hart is not None: break

res = [0, 0, 0, 0, 0]
res[0], res[1] = sum(1 if x == '*' else 0 for x in l[hart[0]][:hart[1]]), sum(1 if x == '*' else 0 for x in l[hart[0]][hart[1] + 1:])

while True:
    now += 1
    if sum(1 if x == '*' else 0 for x in l[now]) >= 2: break
    res[2] += 1

while now < n:
    if l[now][hart[1] - 1] == '*': res[3] += 1
    if l[now][hart[1] + 1] == '*': res[4] += 1

    now += 1

print(*[x + 1 for x in hart])
print(*res)