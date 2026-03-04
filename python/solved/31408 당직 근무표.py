import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from math import ceil

n = int(input())
arr = [*map(int, input().split())]
longest = [0, None]

i = 0
while i < n:
    j = i
    while j < n and arr[j] == arr[i]:
        j += 1
    
    if longest[0] < j - i:
        longest[0], longest[1] = j - i, arr[i]

    i = j

print('YES' if arr.count(longest[1]) <= ceil(n / 2) else 'NO')