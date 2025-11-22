import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

b_cnt = 0
w_cnt = 0

def check(l, value):
    for i in range(len(l)):
        for j in range(len(l[i])):
            if l[i][j] != value: return False
    return True

def f(l):
    if check(l, 1):
        global b_cnt
        b_cnt += 1
        return
    if check(l, 0):
        global w_cnt
        w_cnt += 1
        return
    
    now_div = len(l) // 2
    for i in range(0, len(l), now_div):
        for j in range(0, len(l), now_div):
            start_y, start_x, end_y, end_x = i, j, i + now_div, j + now_div
            t = []
            for k in range(start_y, end_y):
                t.append(l[k][start_x:end_x])
            f(t)

n = int(input())
l = [[int(x) for x in input().split()] for _ in range(n)]

f(l)
print(w_cnt, b_cnt, sep='\n')