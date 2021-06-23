# 1065
n = int(input())
cnt = 0

for i in range(1, n + 1):
    arr = list(map(int, str(i)))

    if i < 100:
        cnt += 1
        continue
    if arr[0] - arr[1] == arr[1] - arr[2]:
        cnt += 1

print(cnt)