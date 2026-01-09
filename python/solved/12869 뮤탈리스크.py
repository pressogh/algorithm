import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

da = [
    [],
    [[-9]],
    [
        [-9, -3],
        [-3, -9]
    ],
    [
        [-9, -3, -1],
        [-9, -1, -3],
        [-3, -9, -1],
        [-3, -1, -9],
        [-1, -9, -3],
        [-1, -3, -9]
    ]
]

n, scv = int(input()), [int(x) for x in input().split()]
se = set()
dq = deque([(tuple(x for x in scv), 0)])
while dq:
    s, count = dq.popleft()

    for att in da[len(s)]:
        ns = tuple(s[i] + att[i] for i in range(len(att)) if s[i] + att[i] > 0)
        if not ns: print(count + 1); exit(0)
        if ns in se: continue
        se.add(ns)
        dq.append((ns, count + 1))