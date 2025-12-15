import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

d, l = dict(), []
res = ["", "", ""]
for i in range(int(input())):
    s, t = input(), ""
    for c in s:
        t += c
        
        if t not in d: d[t] = []
        d[t].append((s, i))

        if len(d[t]) >= 2:
            if len(res[0]) < len(t) or (len(res[0]) == len(t) and d[res[0]][0][1] > d[t][0][1]):
                res[0], res[1], res[2] = t, d[t][0][0], d[t][1][0]
    l.append(s)

if res[0] == '': print(l[0], l[1], sep='\n')
else: print(*res[1:], sep='\n')