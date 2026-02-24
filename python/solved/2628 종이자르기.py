import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
k = int(input())

arr = [[0, n, 0, m]]
while k:
    k -= 1

    r, c = map(int, input().split())

    match r:
        case 0:
            for i in range(len(arr)):
                if arr[i][2] < c < arr[i][2] + arr[i][3]:
                    arr.append([arr[i][0], arr[i][1], c, arr[i][2] + arr[i][3] - c])
                    arr[i][3] = c - arr[i][2]
        case 1:
            for i in range(len(arr)):
                if arr[i][0] < c < arr[i][0] + arr[i][1]:
                    arr.append([c, arr[i][0] + arr[i][1] - c, arr[i][2], arr[i][3]])
                    arr[i][1] = c - arr[i][0]

res = 0
for s in arr:
    res = max(res, s[1] * s[3])
print(res)