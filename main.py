# 4673
def divide(n):
    ans = n
    while n:
        ans += n % 10
        n = n // 10
    return ans

arr = [1 for i in range(10000)]

for i in range(1, 10000):
    if divide(i) >= 9999:
        break
    arr[divide(i)] = 0

for i in range(1, 9995):
    if arr[i] == 1:
        print(i)