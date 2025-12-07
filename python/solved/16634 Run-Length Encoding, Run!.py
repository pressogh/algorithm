import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

cmd, s = input().split()

res = ""
match cmd:
    case 'E':
        i = 0
        while i < len(s):
            j = i
            cnt = 0
            while j < len(s):
                if s[i] != s[j]: break
                cnt += 1
                j += 1
            res += (s[i] + str(cnt))
            i = j
    case 'D':
        for i in range(1, len(s)):
            if i % 2 != 0: res += s[i - 1] * int(s[i])

print(res)