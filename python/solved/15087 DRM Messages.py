import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

s = input()
s1, s2 = s[:len(s) // 2], s[len(s) // 2:]
v1, v2 = sum(ord(x) - ord('A') for x in s1), sum(ord(x) - ord('A') for x in s2)

s1, s2 = [((ord(x) - ord('A')) + v1) % 26 for x in s1], [((ord(x) - ord('A')) + v2) % 26 for x in s2]

res = ""
for i in range(len(s) // 2):
    res += chr((s1[i] + s2[i]) % 26 + ord('A'))
print(res)