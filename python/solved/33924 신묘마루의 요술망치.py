import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(lambda x: int(x) - 1, input().split())
input()

arr = [[i * 2 + j + 1 for j in range(2)] for i in range(4)]
target = arr[n][m]
for cmd in input():
    match cmd:
        case 'A':
            arr[0][0], arr[2][0] = arr[2][0], arr[0][0]
            arr[0][1], arr[2][1] = arr[2][1], arr[0][1]
            arr[1][0], arr[3][0] = arr[3][0], arr[1][0]
            arr[1][1], arr[3][1] = arr[3][1], arr[1][1]
        case 'B':
            arr[0][0], arr[1][1] = arr[1][1], arr[0][0]
            arr[0][1], arr[1][0] = arr[1][0], arr[0][1]
            arr[2][0], arr[3][1] = arr[3][1], arr[2][0]
            arr[2][1], arr[3][0] = arr[3][0], arr[2][1]
        case 'C':
            arr[0][0], arr[3][1] = arr[3][1], arr[0][0]
            arr[0][1], arr[3][0] = arr[3][0], arr[0][1]
            arr[1][0], arr[2][1] = arr[2][1], arr[1][0]
            arr[1][1], arr[2][0] = arr[2][0], arr[1][1]
        case 'D':
            arr[0][0], arr[0][1], arr[1][0], arr[1][1], arr[2][0], arr[2][1], arr[3][0], arr[3][1] = arr[1][0], arr[0][0], arr[2][0], arr[0][1], arr[3][0], arr[1][1], arr[3][1], arr[2][1]

for i in range(4):
    for j in range(2):
        if arr[i][j] == target:
            print(i + 1, j + 1)
            exit(0)