import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
words = [input().zfill(8) for _ in range(n)]

d = dict()
for w in words:
    for i in range(len(w)):
        if w[i] == '0': continue

        if w[i] not in d: d[w[i]] = 0
        d[w[i]] += 10 ** (8 - i)

d = sorted([[x[0], x[1]] for x in d.items()], key=lambda x: x[1])
k = dict()
for i in range(9, 10 - len(d) - 1, -1):
    k[d.pop()[0]] = i

res = 0
for w in words:
    t = 0
    for c in w:
        if c not in k: continue
        t *= 10
        t += k[c]
    res += t
print(res)
