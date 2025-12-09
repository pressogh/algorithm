import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

s = input()
res, i = 0, 0
while True:
    res += 1
    for c in str(res):
        if s[i] != c: continue
        i += 1

        if i < len(s): continue
        print(res)
        exit(0)