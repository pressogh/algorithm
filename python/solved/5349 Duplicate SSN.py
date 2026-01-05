import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

c = Counter()
while True:
    ssn = input()
    if ssn == "000-00-0000": break
    c.update([ssn])
print(*sorted(x[0] for x in c.items() if x[1] >= 2), sep='\n')