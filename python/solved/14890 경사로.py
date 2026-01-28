import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, l = map(int, input().split())
def f(road):
    check = [False] * n
    for i in range(1, n):
        if road[i - 1] > road[i]:
            if road[i - 1] - road[i] != 1 or i + l > n: return False
            for j in range(i, i + l):
                if check[j]: return False
                check[j] = True

    for i in range(n - 1):
        if road[i + 1] > road[i]:
            if road[i + 1] - road[i] != 1 or i - l + 1 < 0: return False
            for j in range(i, i - l, -1):
                if check[j]: return False
                check[j] = True
    return True


arr = [[*map(int, input().split())] for _ in range(n)]

res = 0
for i in range(n):
    res += int(f(arr[i]))
    res += int(f([arr[j][i] for j in range(n)]))
print(res)