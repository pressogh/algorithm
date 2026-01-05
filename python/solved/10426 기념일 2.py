import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from datetime import date, timedelta

d, delta = input().split()
print((date.fromisoformat(d) + timedelta(days=int(delta) - 1)).strftime("%Y-%m-%d"))