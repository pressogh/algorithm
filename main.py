# 2750
n = int(input())
lst = []
while n:
    temp = int(input())
    lst.append(temp)
    n -= 1

print("\n".join(map(str, sorted(lst))))