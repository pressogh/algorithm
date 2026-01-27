import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
arr = [*map(int, input().split())]

one, two, res = set(), set(), 0
for now in arr:
    for o in one:
        if now - o in two: res += 1; break

    one.add(now)
    for o in one: two.add(now + o)

print(res)