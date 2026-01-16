import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

_, s, _ = input(), set(int(x) for x in input().split()), input()
for n in map(int, input().split()):
    print(int(n in s), end=' ')
