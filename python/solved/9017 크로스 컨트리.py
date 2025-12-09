import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t > 0:
    t -= 1

    n = int(input())
    l = [int(x) for x in input().split()]

    c = [0] * (200 + 1)
    for item in l: c[item] += 1
    score = [[0, 0, 0, i] for i in range(200 + 1)]
    s = 1
    for i in range(n):
        if c[l[i]] == 6:
            if score[l[i]][2] < 4: score[l[i]][0] += s
            score[l[i]][2] += 1
            if score[l[i]][2] == 5: score[l[i]][1] = s
            s += 1
    score = sorted([x for x in score if x[0] != 0])
    print(score[0][3])