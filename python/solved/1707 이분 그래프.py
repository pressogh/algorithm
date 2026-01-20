import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def f(n, connect):
    check = [False] * n
    for i in range(n):
        if check[i]: continue

        color, s = [None] * n, [i]
        color[i], check[i] = 0, True
        while s:
            now = s.pop()

            for i in range(len(connect[now])):
                if color[connect[now][i]] is not None and color[now] == color[connect[now][i]]: return False
                if color[connect[now][i]] is None:
                    check[connect[now][i]] = True
                    color[connect[now][i]] = 1 - color[now]
                    s.append(connect[now][i])
        
    return True


t = int(input())
while t:
    t -= 1

    n, m = map(int, input().split())
    connect = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        connect[u].append(v)
        connect[v].append(u)
    
    print('YES' if f(n, connect) else 'NO')