import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
keywords = set([input() for _ in range(n)])

for _ in range(m):
    s = input().split(',')
    for x in s:
        if x in keywords: keywords.remove(x)
    
    print(len(keywords))