import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

s, res = list(input()), 0
while len(s) != 1:
    t = -1
    for i in range(len(s)):
        if s[i] == '1':
            t = i
            break
    
    if t != -1:
        s.pop(t)
        s = list(str(int(''.join(s))))
    else:
        s = list(str(int(''.join(s)) - 1)) 
    res += 1

print(int(s[-1]) + res)