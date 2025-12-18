import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

city = []
while True:
    try:
        s, t = input().split()
        city.append((int(t), s))
    except ValueError: break
city.sort()
print(city[0][1])