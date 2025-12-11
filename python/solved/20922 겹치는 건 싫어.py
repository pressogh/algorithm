import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())
elements = [int(x) for x in input().split()]

count = [0] * (100000 + 1)
count[elements[0]] += 1

s, e, res = 0, 1, 0
while e < n:
    now = elements[e]
    count[now] += 1
    if count[now] > k:
        while count[now] > k:
            count[elements[s]] -= 1
            s += 1
    
    res = max(res, e - s + 1)
    e += 1
print(res)
