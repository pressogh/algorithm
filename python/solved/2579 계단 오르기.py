import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

"""
https://daimhada.tistory.com/181
"""
def solve():
    n = int(input())
    l = [int(input()) for _ in range(n)]
    if len(l) <= 2:
        print(sum(l))
        return
    
    dp = [0] * n
    dp[0], dp[1] = l[0], l[0] + l[1]
    for i in range(2, n):
        dp[i] = max(dp[i - 3] + l[i - 1] + l[i], dp[i - 2] + l[i])
    print(dp[-1])

if __name__ == '__main__':
    solve()
