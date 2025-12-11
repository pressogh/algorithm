import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, balls = int(input()), input()

last = n - 1
while last >= 0 and balls[last] == balls[-1]:
    last -= 1
if last == 0:
    print(0)
    exit(0)

first = 0
while first < n and balls[first] == balls[0]:
    first += 1

r, b = 0, 0
for ball in balls[:last + 1]:
    match ball:
        case 'R': r += 1
        case 'B': b += 1
res = min(r, b)
r, b = 0, 0
for ball in balls[first:]:
    match ball:
        case 'R': r += 1
        case 'B': b += 1
print(min(res, r, b))