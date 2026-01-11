import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

s = input()
words = [input() for _ in range(int(input()))]
dp = [0] * (len(s) + 1)
dp[0] = 1

for i in range(len(s)):
    if not dp[i]: continue

    for w in words:
        if s[i:i+len(w)] == w:
            dp[i + len(w)] = 1
print(dp[-1])