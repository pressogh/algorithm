import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import re

s = re.split(r'(\+|\-)', input())

res = [0]
for item in s:
    match item:
        case '+': pass
        case '-': res.append(0)
        case _: res[-1] += int(item)

print(res[0] - sum(res[1:]))