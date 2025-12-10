import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())

rooms = []
for _ in range(n):
    lv, name = input().split()
    lv = int(lv)

    flag = False
    for room in rooms:
        if abs(lv - room[0][0]) <= 10 and len(room) < m:
            room.append((lv, name))
            flag = True
            break
    if not flag: rooms.append([(lv, name)])

for room in rooms:
    print("Started!" if len(room) == m else "Waiting!")
    for user in sorted(room, key=lambda x: x[1]):
        print(*user)