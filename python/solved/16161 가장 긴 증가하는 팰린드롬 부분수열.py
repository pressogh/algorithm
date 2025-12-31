import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, arr = int(input()), [int(x) for x in input().split()]
s, e, res = 0, 0, 0
while s < n:
    e = s
    while e + 1 < n and arr[e + 1] == arr[s] and e - s < 1:
        e += 1
    
    i, j = s - 1, e + 1
    v = arr[s]
    while i >= 0 and j < n and arr[i] == arr[j] and arr[i] < v:
        v = arr[i]
        i -= 1
        j += 1
    res = max(res, j - i - 1)
    s = j
print(res)