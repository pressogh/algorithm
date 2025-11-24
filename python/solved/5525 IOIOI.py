import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, _, s = int(input()), input(), input()

now, res, cnt = 0, 0, 0
while now <= len(s):
    if s[now:now + 3] == 'IOI':
        now += 2
        cnt += 1
        if cnt == n:
            res += 1
            cnt -= 1
    else:
        now += 1
        cnt = 0

print(res)