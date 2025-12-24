import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

res = 0
for _ in range(int(input())):
    s = input()
    stk = []
    for c in s:
        if not stk: stk.append(c); continue
        if stk[-1] == c: stk.pop()
        else: stk.append(c)
    if not stk: res += 1
print(res)