import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def f(l, t):
    c = 0
    for i in range(1, len(l)):
        if l[i - 1] == t[i - 1]: continue
        c += 1
        for j in range(i - 1, min(i + 2, len(l))): l[j] = 1 - l[j]
    return c if l == t else 2 ** 31

n = int(input())
s1, s2 = [int(x) for x in input()], [int(x) for x in input()]

res = f(s1[:], s2)
s1[0], s1[1] = 1 - s1[0], 1 - s1[1]
res = min(res, f(s1, s2) + 1)
print(res if res < 2 ** 31 else -1)