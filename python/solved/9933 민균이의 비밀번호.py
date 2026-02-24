import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
arr = set()
while n:
    n -= 1
    
    s = input()
    if s[::-1] in arr or s == s[::-1]:
        print(len(s), s[len(s) // 2])
        break
    arr.add(s)