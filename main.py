# 1929
arr = [1 for x in range(1000001)]

for i in range(2, 1000001):
    if arr[i] == 0:
        continue
    for j in range(2 * i, 1000001, i):
        if arr[j] == 0:
            continue
        arr[j] = 0

n, m = input().split()
n = int(n)
m = int(m)

arr[0] = 0
arr[1] = 0
for i in range(n, m + 1):
    if arr[i] == 1:
        print(f'{i}')