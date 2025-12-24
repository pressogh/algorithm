import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

res = ['', 0, 0]
for _ in range(int(input())):
    team, *problems = input().split()
    c, m = 0, 0
    if problems[1] != '0':
        c += 1
        m += int(problems[1]) + (int(problems[0]) - 1) * 20
    if problems[3] != '0':
        c += 1
        m += int(problems[3]) + (int(problems[2]) - 1) * 20
    if problems[5] != '0':
        c += 1
        m += int(problems[5]) + (int(problems[4]) - 1) * 20
    if problems[7] != '0':
        c += 1
        m += int(problems[7]) + (int(problems[6]) - 1) * 20
    
    if res[1] < c:
        res[0], res[1], res[2] = team, c, m
    elif res[1] == c and m < res[2]:
        res[0], res[2] = team, m
print(*res)