import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

from collections import Counter

n = int(input())
s = input()
count = Counter(s)
count.update('ACGT')

dna, c = '', 2 ** 31
for item in count.items():
    if item[1] < c:
        dna, c = item

print(c - 1)
print(dna * n)