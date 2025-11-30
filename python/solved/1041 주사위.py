import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
sys.setrecursionlimit(10 ** 6)

n = int(input())
dice = [int(x) for x in input().split()]

if n == 1:
    print(sum(dice) - max(dice))
    exit(0)

memo = [0, 0, 0, 0]
memo[1] = min(dice)
memo[2] = min(
    dice[0] + dice[1],
    dice[0] + dice[2],
    dice[0] + dice[3],
    dice[0] + dice[4],
    dice[1] + dice[2],
    dice[1] + dice[3],
    dice[1] + dice[5],
    dice[2] + dice[4],
    dice[2] + dice[5],
    dice[3] + dice[4],
    dice[3] + dice[5],
    dice[4] + dice[5]
)
memo[3] = min(
    dice[0] + dice[1] + dice[2],
    dice[0] + dice[1] + dice[3],
    dice[0] + dice[2] + dice[4],
    dice[0] + dice[3] + dice[4],
    dice[1] + dice[2] + dice[5],
    dice[1] + dice[3] + dice[5],
    dice[2] + dice[4] + dice[5],
    dice[3] + dice[4] + dice[5]
)

print(memo[3] * 4 + memo[2] * ((n - 1) * 2 * 4 - 4) + memo[1] * (((n - 1) * (n - 2) * 4) + (n - 2) ** 2))
