import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

arr, s = input(), []
for now in arr:
    match now:
        case '(': s.append('(')
        case '[': s.append('[')
        case ')':
            t = 0
            while True:
                if not s or s[-1] in (')', '[', ']'):
                    print(0)
                    exit(0)
                
                last = s.pop()
                if last == '(': break
                t += last
            if t == 0: s.append(2)
            else: s.append(t * 2)
        case ']':
            t = 0
            while True:
                if not s or s[-1] in ('(', ')', ']'):
                    print(0)
                    exit(0)
                
                last = s.pop()
                if last == '[': break
                t += last
            if t == 0: s.append(3)
            else: s.append(t * 3)

if all(x not in ('(', ')', '[', ']') for x in s): print(sum(s))
else: print(0)