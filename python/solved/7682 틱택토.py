import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

table = [
    [[1, 1, 1], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
    [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
    [[0, 0, 1], [0, 0, 1], [0, 0, 1]],
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
]
def f(s, c):
    for w in table:
        flag = True
        for i in range(3):
            for j in range(3):
                if w[i][j] == 1 and s[i * 3 + j] != c: flag = False
        if flag: return True
    return False

while True:
    s = input()
    if s == 'end': break

    c = 0
    for x in s: c += 1 if x == 'X' else -1 if x == 'O' else 0
    if c != 1 and c != 0: print('invalid'); continue

    f_w, s_w = f(s, 'X'), f(s, 'O')
    if f_w and s_w: print('invalid'); continue
    if not f_w and not s_w: print('invalid' if '.' in s else 'valid'); continue

    if f_w: print('invalid' if c == 0 else 'valid')
    else: print('invalid' if c == 1 else 'valid')