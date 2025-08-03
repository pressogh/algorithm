# 2180
n = int(input())
lst = []
for i in range(n):
    a, b = map(int, input().split())
    if a == 0:
        lst.append((float('inf'), a, b))
    else:
        lst.append((b / a, a, b))

lst.sort()
ans = 0
t = 0
for i in range(n):
    ans += lst[i][1] * t + lst[i][2]
    ans %= 40000
    t = ans

print(ans)
print(lst)