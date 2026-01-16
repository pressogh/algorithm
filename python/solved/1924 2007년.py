import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from datetime import datetime

date = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

x, y = map(int, input().split())
now = datetime(year=2007, month=x, day=y)
print(date[now.weekday()])
