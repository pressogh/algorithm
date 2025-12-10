import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

import string
from collections import Counter

def check(s1, s2):
    c1, c2 = Counter(s1 + ''.join(string.ascii_uppercase)), Counter(s2 + ''.join(string.ascii_uppercase))
    diff_cnt = 0
    for s in string.ascii_uppercase:
        c = abs(c1.get(s) - c2.get(s))

        if c == 0: continue
        elif c == 1: diff_cnt += 1
        else: return 0

    if diff_cnt == 0: return 1
    if len(s1) == len(s2): return 1 if diff_cnt == 2 else 0
    return 1 if diff_cnt == 1 else 0

n = int(input())
s = input()
res = 0
for _ in range(n - 1): res += check(s, input())
print(res)