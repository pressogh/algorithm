import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

mw, mb = map(int, input().split())
tw, tb = map(int, input().split())
pw, pb = map(int, input().split())

white_start_max = min(mw, tb, pw)
black_start_max = min(mb, tw, pb)
print(min(white_start_max, black_start_max) * 2 + (1 if white_start_max != black_start_max else 0))