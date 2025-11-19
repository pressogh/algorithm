import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    dp = [(1, 0), (0, 1)]
    for _ in range(2, 40 + 1):
        dp.append((dp[-1][0] + dp[-2][0], dp[-1][1] + dp[-2][1]))

    t = int(input())
    while t > 0:
        print(*dp[int(input())])
        t -= 1

if __name__ == '__main__':
    solve()