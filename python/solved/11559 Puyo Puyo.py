import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

arr = [list(input()) for _ in range(12)]
res = 0
while True:
    flag = False
    
    for i in range(12):
        for j in range(6):
            if arr[i][j] == '.': continue
            s, check = [(i, j)], set([(i, j)])
            while s:
                y, x = s.pop()

                for k in range(4):
                    ny, nx = y + dy[k], x + dx[k]
                    if 0 <= ny < 12 and 0 <= nx < 6 and (ny, nx) not in check and arr[y][x] == arr[ny][nx]:
                        check.add((ny, nx))
                        s.append((ny, nx))
            
            if len(check) < 4: continue
            flag = True
            for c in check: arr[c[0]][c[1]] = '.'

    if not flag: break
    res += 1

    for i in range(11, 0, -1):
        for j in range(6):
            if arr[i][j] != '.': continue
            k = i
            while True:
                if k <= 0 or arr[k][j] != '.': break
                k -= 1
            arr[i][j], arr[k][j] = arr[k][j], '.'

print(res)