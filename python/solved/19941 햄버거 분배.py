import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, k = map(int, input().split())
s = input()

res = 0
eat = [False] * n
for i in range(n):
    if s[i] == 'H': continue

    flag = False
    for j in range(max(0, i - k), i):
        if s[j] == 'H' and not eat[j]:
            eat[j] = True
            flag = True
            break
    if not flag:
        for j in range(i + 1, min(n, i + k + 1)):
            if s[j] == 'H' and not eat[j]:
                eat[j] = True
                flag = True
                break
    
    if flag: res += 1
print(res)