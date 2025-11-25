import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import deque

t = int(input())
while t > 0:
    t -= 1
    func, _ = input(), input()
    arr = input()[1:-1]
    dq = deque(arr.split(',')) if len(arr) > 0 else deque()

    has_err, rev = False, False
    i = 0
    while i < len(func):
        now_cmd = func[i]

        j = i
        while j < len(func) and func[j] == now_cmd:
            j += 1

        count = j - i
        match now_cmd:
            case 'R':
                if count % 2 != 0: rev = not rev
            case 'D':
                if count > len(dq):
                    print('error')
                    has_err = True
                    break
                else:
                    for _ in range(count):
                        if not rev: dq.popleft()
                        else: dq.pop()
        i += count
    
    if not has_err:
        print('[', end='')
        if not rev:
            for i in range(len(dq)):
                print(dq[i], end=',' if i != len(dq) - 1 else '')
        else:
            for i in range(len(dq) - 1, -1, -1):
                print(dq[i], end=',' if i != 0 else '')
        print(']')