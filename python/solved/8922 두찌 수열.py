import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t:
    t -= 1

    n = int(input())
    memo, arr = set(), tuple(map(int, input().split()))
    while True:
        
        nxt = []
        for i in range(n - 1):
            nxt.append(abs(arr[i] - arr[i + 1]))
        nxt.append(abs(arr[-1] - arr[0]))
        arr = tuple(nxt)

        if all(x == 0 for x in arr):
            print('ZERO')
            break
        if arr in memo:
            print('LOOP')
            break

        memo.add(arr)