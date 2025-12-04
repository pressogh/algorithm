import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

t = int(input())
while t > 0:
    t -= 1

    s = input()
    left, right = [], []
    for item in s:
        match item:
            case '>':
                if right: left.append(right.pop())
            case '<':
                if left: right.append(left.pop())
            case '-':
                if left: left.pop()
            case _:
                left.append(item)
    
    s = left + right[::-1]
    print(''.join(s))