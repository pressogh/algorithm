# 1371
import collections
import sys
import re

lines = sys.stdin.read()
lines = re.sub(" |\n", '', lines)
lines = collections.Counter(lines).most_common()
lines.sort(key=lambda x: (x[1], x[0]))

temp = lines[len(lines) - 1][1]
i = len(lines) - 1
lst = []
while 1:
    if i < 0:
        break
    if lines[i][1] != temp:
        break

    lst.append(lines[i][0])
    i -= 1

lst.reverse()
print("".join(map(str, lst)))