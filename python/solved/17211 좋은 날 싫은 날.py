import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, today = map(int, input().split())
arr = [*map(float, input().split())]
if today:
    good_prob, bad_prob = arr[2], arr[3]
else:
    good_prob, bad_prob = arr[0], arr[1]

n -= 1
while n:
    n -= 1
    good_prob, bad_prob = good_prob * arr[0] + bad_prob * arr[2], good_prob * arr[1] + bad_prob * arr[3]

print(round(good_prob * 1000), round(bad_prob * 1000), sep='\n')