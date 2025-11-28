import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
sys.setrecursionlimit(10 ** 6)

tree = [int(x) for x in sys.stdin.readlines()]

def post(arr):
    if len(arr) == 0: return

    l, r = [], []
    root = arr[0]
    for i in range(1, len(arr)):
        if root < arr[i]:
            l = arr[1:i]
            r = arr[i:]
            break
    else: l = arr[1:]

    post(l)
    post(r)
    print(root)

post(tree)