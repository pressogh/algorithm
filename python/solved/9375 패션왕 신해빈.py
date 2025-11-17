import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

def solve():
    for _ in range(int(input())):
        d = dict()

        for _ in range(int(input())):
            _, ware = input().split()
            d[ware] = d[ware] + 1 if ware in d else 1

        res = 1
        for key in d:
            # 해당 타입의 의상을 입는 경우(d[key]) + 해당 의상을 안입는 경우(1) -> d[key] + 1
            res *= (d[key] + 1)
        print(res - 1)

if __name__ == '__main__':
    solve()