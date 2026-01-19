import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

log = []

def hanoi(remain, f, t, v):
    if remain == 1: log.append((f, t)); return

    hanoi(remain - 1, f, v, t)
    log.append((f, t))
    hanoi(remain - 1, v, t, f)


n = int(input())

hanoi(n, 1, 3, 2)
print(len(log))
for l in log: print(*l)