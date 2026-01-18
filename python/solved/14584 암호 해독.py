import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def f(s, n):
    return "".join([chr(((ord(c) - ord('a')) + n) % 26 + ord('a')) for c in s])

s = input()
words = [input() for _ in range(int(input()))]

for i in range(27):
    shifted_s = f(s, i)
    for w in words:
        if w in shifted_s: print(shifted_s); exit(0)