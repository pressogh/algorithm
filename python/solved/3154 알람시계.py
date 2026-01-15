import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

coor = [
    [1, 3],
    [0, 0],
    [1, 0],
    [2, 0],
    [0, 1],
    [1, 1],
    [2, 1],
    [0, 2],
    [1, 2],
    [2, 2]
]

hhmm = input()
h_list, m_list = [int(hhmm[:2])], [int(hhmm[3:])]
while True:
    t = h_list[-1] + 24
    if t >= 100: break
    h_list.append(t)
while True:
    t = m_list[-1] + 60
    if t >= 100: break
    m_list.append(t)

res = [1 << 31, '']
for h in h_list:
    for m in m_list:
        t = str(h).zfill(2) + str(m).zfill(2)
        effort = 0
        for i in range(1, 4):
            effort += abs(coor[int(t[i])][0] - coor[int(t[i - 1])][0]) + abs(coor[int(t[i])][1] - coor[int(t[i - 1])][1])
        if effort < res[0]:
            res[0], res[1] = effort, f"{t[:2]}:{t[2:]}"

print(res[1])