# 5635
import sys                  # 여러줄 입력
input = sys.stdin.readline

lst = []
for _ in range(int(input())):
    a, b, c, d = map(str, input().split())
    lst.append([a, b, c, d])

lst.sort(key=lambda x: (int(x[3]), int(x[2]), int(x[1])))
print(lst[-1][0])
print(lst[0][0])