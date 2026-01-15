import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

sq = [5]
while sq[-1] * 5 <= 10 ** 6:
    sq.append(sq[-1] * 5)
i = 1
while True:
    n = int(input())
    if n == 0: break

    t = 0
    for s in sq: t += n // s
    print(f"Case #{i}: {t}")
    i += 1