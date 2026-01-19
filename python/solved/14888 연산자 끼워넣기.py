import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
nums, op = [*map(int, input().split())], [*map(int, input().split())]

res = [-1 * (1 << 31), (1 << 31)]


def dfs(depth, now):
    if depth >= n - 1:
        res[0], res[1] = max(res[0], now), min(res[1], now)
        return
    
    if op[0] > 0:
        op[0] -= 1
        dfs(depth + 1, now + nums[depth + 1])
        op[0] += 1
    if op[1] > 0:
        op[1] -= 1
        dfs(depth + 1, now - nums[depth + 1])
        op[1] += 1
    if op[2] > 0:
        op[2] -= 1
        dfs(depth + 1, now * nums[depth + 1])
        op[2] += 1
    if op[3] > 0:
        op[3] -= 1
        dfs(depth + 1, (abs(now) // nums[depth + 1]) * (-1 if now <= 0 else 1))
        op[3] += 1


dfs(0, nums[0])
print(*res, sep='\n')