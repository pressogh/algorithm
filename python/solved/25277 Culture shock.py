import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

_, s = input(), input().split()
res = sum(1 if c in ('she', 'he', 'him', 'her') else 0 for c in s)
print(res)