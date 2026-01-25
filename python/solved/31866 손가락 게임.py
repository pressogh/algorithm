import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

j, i = map(int, input().split())

res = ''
if j in (0, 2, 5) and i in (0, 2, 5):
    if j == 0 and i == 0: res = '='
    elif j == 0 and i == 2: res = '>'
    elif j == 0 and i == 5: res = '<'
    elif j == 2 and i == 0: res = '<'
    elif j == 2 and i == 2: res = '='
    elif j == 2 and i == 5: res = '>'
    elif j == 5 and i == 0: res = '>'
    elif j == 5 and i == 2: res = '<'
    elif j == 5 and i == 5: res = '='
elif j in (0, 2, 5) and i not in (0, 2, 5): res = '>'
elif j not in (0, 2, 5) and i in (0, 2, 5): res = '<'
else: res = '='

print(res)