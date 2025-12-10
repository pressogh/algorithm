import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

s = list(input())
c = [0, 0]
for x in s: c[ord(x) - ord('0')] += 1
c[0], c[1] = c[0] // 2, c[1] // 2

now = 0
while c[1] > 0:
    if s[now] == '1':
        del s[now]
        c[1] -= 1
    else: now += 1

now = len(s) - 1
while c[0] > 0:
    if s[now] == '0':
        del s[now]
        c[0] -=1
    now -= 1

print(''.join(s))