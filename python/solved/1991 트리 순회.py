import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

n = int(input())
tree = dict()

for _ in range(n):
    p, ln, rn = input().split()
    tree[p] = [ln, rn]

def front(now):
    left, right = tree[now]
    print(now, end='')
    if left != '.': front(left)
    if right != '.': front(right)

def middle(now):
    left, right = tree[now]
    if left != '.': middle(left)
    print(now, end='')
    if right != '.': middle(right)

def back(now):
    left, right = tree[now]
    if left != '.': back(left)
    if right != '.': back(right)
    print(now, end='')

front('A')
print()
middle('A')
print()
back('A')
