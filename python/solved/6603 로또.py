import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from itertools import combinations

while True:
    lotto = [int(x) for x in input().split()[1:]]
    if not lotto: break
    
    for comb in combinations(lotto, 6):
        print(*comb)
    print()