import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

s = input()
if len(s) == 4: print(20)
elif len(s) == 3:
    if s[0] == '1' and s[1] == '0': print(10 + int(s[2]))
    else: print(10 + int(s[0]))
else: print(int(s[0]) + int(s[1]))