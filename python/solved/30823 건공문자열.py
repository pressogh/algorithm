import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())
arr = input()

if k == 1: print(arr)
elif (n - k) % 2: print(arr[k - 1:] + arr[:k - 1])
else: print(arr[k - 1:] + arr[k - 2::-1])