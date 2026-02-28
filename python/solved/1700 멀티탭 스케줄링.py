import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())
arr = [*map(int, input().split())]

res, now = 0, set()


def get_min_v(idx):
    res = []
    for e in now:
        t = 0
        for i in range(idx + 1, k):
            if arr[i] != e: continue
            t |= (1 << (k - i))
        res.append((t, e))
    res.sort()
    return res[0][1]


for i in range(k):
    if arr[i] in now: continue
    if len(now) < n:
        now.add(arr[i])
        continue
    
    res += 1
    now.remove(get_min_v(i))
    now.add(arr[i])

print(res)