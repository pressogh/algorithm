import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, u, l = map(int, input().split())
if n >= 1000:
    if (u >= 8000 or l >= 260):
        print("Very Good")
    else:
        print("Good")
else:
    print("Bad")