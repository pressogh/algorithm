import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from itertools import combinations

n = int(input())
table = [[*map(int, input().split())] for _ in range(n)]


def f(s, l):
    s_sum, l_sum = 0, 0

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            s_sum += table[s[i]][s[j]] + table[s[j]][s[i]]
            l_sum += table[l[i]][l[j]] + table[l[j]][l[i]]
    
    return abs(s_sum - l_sum)


s, res = set(range(n)), 1 << 31
for c in combinations(range(n), r=n//2):
    start_team = set(c)
    link_team = s - start_team

    res = min(res, f(tuple(start_team), tuple(link_team)))

print(res)