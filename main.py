# 10250
tmp = int(input())
t2 = 0

while tmp:
    h, w, n = map(int, input().split())
    t3 = 0

    for i in range(1, w + 1):
        for j in range(1, h + 1):
            t2 = 100 * j + i

            t3 += 1
            if t3 >= n:
                break
        if t3 >= n:
            break
    print(t2)
    tmp -= 1
