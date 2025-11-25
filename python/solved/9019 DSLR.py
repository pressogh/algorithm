import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

t = int(input())
while t > 0:
    t -= 1

    a, b = map(int, input().split())

    dq = deque([(a, "")])

    res = "A" * 32
    check = [False] * 10000
    check[a] = True
    while dq:
        now, calc = dq.popleft()
        
        now_str = str(now).zfill(4)
        calc_now = [
            (now * 2 % 10000, 'D'),
            (now - 1 if now != 0 else 9999, 'S'),
            (int(now_str[1:] + now_str[0]), 'L'),
            (int(now_str[-1] + now_str[:-1]), 'R')
        ]

        found = False
        for i in range(4):
            next_now, next_calc = calc_now[i][0], calc + calc_now[i][1]
            if len(res) <= len(next_calc) or check[next_now]: continue

            check[next_now] = True
            if next_now == b:
                print(next_calc)
                found = True
                break
            dq.append((next_now, next_calc))
        if found: break