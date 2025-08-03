# Lonely Photo
# 11번 테스트케이스 빼고 다 됨
import sys                  # 여러줄 입력
input = sys.stdin.readline

n = int(input())
s = list(input().rstrip())

cnt = 0
for i in range(3, n + 1):
    flag = False
    left, right = 0, i - 1
    gcnt, hcnt = 0, 0

    for j in range(i):
        if s[j] == 'G':
            gcnt += 1
        elif s[j] == 'H':
            hcnt += 1
    
    while True:
        if (gcnt > 1 and hcnt == 1) or (gcnt == 1 and hcnt > 1):
            cnt += 1
            flag = True

        if s[left] == 'G':
            gcnt -= 1
        elif s[left] == 'H':
            hcnt -= 1
        
        left += 1
        right += 1

        if right > n - 1:
            break

        if s[right] == 'G':
            gcnt += 1
        elif s[right] == 'H':
            hcnt += 1
    if not flag:
        break
        
print(cnt)