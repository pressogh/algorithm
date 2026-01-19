import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n, m = map(int, input().split())
books = [int(x) for x in input().split()]

pos, neg, last = [], [], 0
for book in books:
    last = max(abs(book), last)
    if book > 0: pos.append(book)
    else: neg.append(abs(book))

pos.sort(reverse=True)
neg.sort(reverse=True)

res = 0
for i in range(0, len(pos), m): res += pos[i] * 2
for i in range(0, len(neg), m): res += neg[i] * 2

print(res - last)