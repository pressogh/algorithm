import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def f(s, name):
    for i in range(len(s)):
        for j in range(1, len(s) - i):
            t = ""
            for k in range(i, len(s), j):
                t += s[k]
                if t == name: return True
    return False


n, name = int(input()), input()

res = 0
while n > 0:
    n -= 1
    s = input()

    if f(s, name): res += 1

print(res)