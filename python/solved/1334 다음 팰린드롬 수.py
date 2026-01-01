import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

s = input()
n = len(s)
half = s[:(n + 1) // 2]

if s == "9" * n: print(int(s) + 2)
elif n == 1: print(int(s) + 1)
elif n % 2 != 0:
    t = half + half[-2::-1]
    if int(t) > int(s): print(t)
    else:
        t = str(int(half) + 1)
        t = t + t[-2::-1]
        print(t)
else:
    t = half + half[::-1]
    if int(t) > int(s): print(t)
    else:
        t = str(int(half) + 1)
        t = t + t[::-1]
        print(t)