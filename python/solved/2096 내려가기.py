import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

mid, mad = [[0] * 3 for _ in range(2)], [[0] * 3 for _ in range(2)]
for i in range(int(input())):
    a, b, c = map(int, input().split())

    if i == 0:
        mid[1][0], mid[1][1], mid[1][2] = a, b, c
        mad[1][0], mad[1][1], mad[1][2] = a, b, c
        continue

    mid[0][0], mid[0][1], mid[0][2] = mid[1][0], mid[1][1], mid[1][2]
    mad[0][0], mad[0][1], mad[0][2] = mad[1][0], mad[1][1], mad[1][2]

    mid[1][0] = min(mid[0][0], mid[0][1]) + a
    mid[1][1] = min(mid[0][0], mid[0][1], mid[0][2]) + b
    mid[1][2] = min(mid[0][1], mid[0][2]) + c
    mad[1][0] = max(mad[0][0], mad[0][1]) + a
    mad[1][1] = max(mad[0][0], mad[0][1], mad[0][2]) + b
    mad[1][2] = max(mad[0][1], mad[0][2]) + c

print(max(mad[-1]), min(mid[-1]))