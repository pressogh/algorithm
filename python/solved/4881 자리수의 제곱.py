import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

while True:
    a, b = map(int, input().split())
    if a == b == 0: break

    res = [a, b, 1 << 31]

    a_cycle, b_cycle = False, False
    da, db = dict(), dict()
    da[a], db[b] = 1, 1
    while True:
        if not a_cycle:
            ta = 0
            for t in str(a): ta += int(t) ** 2

        if not b_cycle:
            tb = 0
            for t in str(b): tb += int(t) ** 2

        if ta in da: a_cycle = True
        else:
            da[ta] = da[a] + 1
            a = ta

        if tb in db: b_cycle = True
        else:
            db[tb] = db[b] + 1
            b = tb
        
        if a_cycle and b_cycle: break
    
    for k, v in da.items():
        if k in db: res[2] = min(res[2], v + db[k])

    res[2] = res[2] if res[2] != 1 << 31 else 0
    print(*res)

