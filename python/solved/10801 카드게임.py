import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

a_cards, b_cards = map(int, input().split()), map(int, input().split())
ac, bc = 0, 0
for a, b in zip(a_cards, b_cards):
    if a > b: ac += 1
    elif a < b: bc += 1

if ac > bc: print('A')
elif ac < bc: print('B')
else: print('D')