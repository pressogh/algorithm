import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

e, s, m = map(int, input().split())

y, i = [0, 0, 0], 0
while True:
    i += 1
    y[0] += 1
    if y[0] >= 16: y[0] = 1

    y[1] += 1
    if y[1] >= 29: y[1] = 1

    y[2] += 1
    if y[2] >= 20: y[2] = 1

    if y[0] == e and y[1] == s and y[2] == m:
        print(i)
        break