import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t:
    t -= 1
    n = int(input())
    arr = [*map(int, input().split())]

    s = dict()
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            k = arr[i] + arr[j]
            if k not in s: s[k] = 0
            s[k] += 1
    
    res = 0
    for i in range(len(arr)):
        if arr[i] * 2 in s: res += s[arr[i] * 2]
    print(res)