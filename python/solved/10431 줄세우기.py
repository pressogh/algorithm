import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

p = int(input())
while p > 0:
    p -= 1

    l = [int(x) for x in input().split()]
    t, l = l[0], l[1:]

    res = 0
    for i in range(20 - 1, -1, -1):
        for j in range(i - 1, -1, -1):
            if l[i] < l[j]: res += 1
    print(t, res)