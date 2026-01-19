import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))


n, m, l = map(int, input().split())
arr = sorted([0] + [*map(int, input().split())] + [l])


def f(now):
    res = 0
    for i in range(len(arr) - 1):
        if not ((arr[i + 1] - arr[i]) % now): res += (arr[i + 1] - arr[i]) // now - 1
        else: res += (arr[i + 1] - arr[i]) // now
    return res


s, e, res = 1, l - 1, 1 << 31
while s < e:
    mid = (s + e) // 2

    t = f(mid)
    if t > m: s = mid + 1
    else:
        if t <= m: res = min(res, mid)
        e = mid

print(res)