import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def f(s, c, k):
    start, end = 0, 0
    cnt, r1, r2 = 0, 2 ** 31, 0
    while end < len(s):
        if s[end] == c: cnt += 1

        if cnt == k:
            while s[start] != c: start += 1
            r1 = min(r1, end - start + 1)
            r2 = max(r2, end - start + 1)
            start, cnt = start + 1, cnt - 1
        end += 1
    return [r1, r2]

t = int(input())
while t > 0:
    t -= 1

    s, k = input(), int(input())
    c = [0] * (ord('z') - ord('a') + 1)
    for x in s: c[ord(x) - ord('a')] += 1

    if all(x < k for x in c): print(-1); continue

    c = [chr(i + ord('a')) for i in range(len(c)) if c[i] >= k]
    r1, r2 = 2 ** 31, 0
    for x in c:
        r = f(s, x, k)
        r1, r2 = min(r1, r[0]), max(r2, r[1])
    print(r1, r2)