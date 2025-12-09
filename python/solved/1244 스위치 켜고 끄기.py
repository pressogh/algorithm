import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
switches = [int(x) for x in input().split()]

for _ in range(int(input())):
    s, v = map(int, input().split())
    match s:
        case 1:
            i = 1
            while v * i < len(switches) + 1:
                now = v * i - 1
                if switches[now] == 0: switches[now] = 1
                else: switches[now] = 0
                i += 1
        case 2:
            v -= 1
            c = 0
            while True:
                c += 1
                if v - c < 0 or v + c > len(switches) or switches[v-c:v][::-1] != switches[v+1:v+c+1]:
                    c -= 1
                    break
            for i in range(v - c, v + c + 1):
                if switches[i] == 0: switches[i] = 1
                else: switches[i] = 0

for i in range(n):
    print(switches[i], end=' ')
    if (i + 1) % 20 == 0: print()