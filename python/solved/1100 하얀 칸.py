import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

board = [input() for _ in range(8)]

res = 0
for i in range(8):
    if not i % 2:
        res += board[i][::2].count('F')
    else:
        res += board[i][1::2].count('F')
print(res)