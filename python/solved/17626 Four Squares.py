import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

pre = [x ** 2 for x in range(1, 225)]

def solve():
    n = int(input())
    if n < 4:
        print(n)
        return
    dp = [0] + [4] * n
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3

    sq = 1
    for i in range(4, n + 1):
        if pre[sq] == i:
            dp[i] = 1
            sq += 1
            continue
        
        for j in range(sq, 0, -1):
            dp[i] = min(dp[i], dp[i - pre[j - 1]] + 1)
            if dp[i] <= 2:
                break
    print(dp[-1])

if __name__ == '__main__':
    solve()