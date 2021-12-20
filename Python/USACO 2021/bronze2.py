# Air Cownditioning
# 1번 테스트케이스만 됨
import sys                  # 여러줄 입력
input = sys.stdin.readline

'''
5
1 5 3 3 4
1 2 2 2 1

0 3 1 1 3

0 2 0 0 2
0 1 0 0 2
0 0 0 0 2
0 0 0 0 1
0 0 0 0 0

0   3   1   1   3

0   2   0   0   2
0   1   -1  -1  1
0   0   -2  -2  0
0   0   -1  -1  0
0   0   0   0   0

5
1 5 3 3 1
1 2 2 2 5

0   3   1   1   2

0   2   0   0   1
0   1   -1  -1  0
0   0   -2  -2  0
0   0   -1  -1  0
0   0   0   0   0

5
4 5 3 3 1
1 2 2 2 5

3   3   1   1   -4

2   2   0   0   -4
1   1   -1  -1  -4
0   0   -2  -2  -4
0   0   -1  -1  -3
0   0   0   0   -2
0   0   0   0   -1
0   0   0   0   0
'''

n = int(input())
want = list(map(int, input().rstrip().split()))
now = list(map(int, input().rstrip().split()))

ans = 0
left = 0
while want != now:    
    if want[left] - now[left] != 0:
        if left >= n - 1:
            right = left
        else:
            right = left + 1
        if want[left] - now[left] > 0:
            while True:
                if want[right] - now[right] < 0 or want[right] == now[right] or right >= n - 1:
                    break
                right += 1
        elif want[left] - now[left] < 0:
            while True:
                if want[right] - now[right] > 0 or want[right] == now[right] or right >= n - 1:
                    break
                right += 1
    
        ans += abs(want[left] - now[left])
        tmp = want[left] - now[left]

        for i in range(left, right + 1):
            now[i] += tmp
        print(now)
    else:
        left += 1
print(ans)