import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t > 0:
    t -= 1

    n, k, team_id, m = map(int, input().split())
    l = [[[0] * k, 0, 0, i] for i in range(1, n + 1)]
    for i in range(m):
        team, problem, point = map(int, input().split())
        team -= 1
        problem -= 1
        
        l[team][0][problem] = max(l[team][0][problem], point)
        l[team][1] += 1
        l[team][2] = i
    l.sort(key=lambda x: (-sum(x[0]), x[1], x[2]))
    for i in range(n):
        if l[i][3] == team_id:
            print(i + 1)
            break