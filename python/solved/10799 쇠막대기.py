import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

exp, s, res = input(), [], 0
for i in range(len(exp)):
    match exp[i]:
        case '(': s.append('(')
        case ')':
            s.pop()
            if exp[i - 1] == '(': res += len(s)
            else: res += 1

print(res)