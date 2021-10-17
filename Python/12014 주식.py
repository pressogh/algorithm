# 12014
import sys                  # 여러줄 입력
import bisect               # 이진 탐색
input = sys.stdin.readline

for t in range(int(input())):
    n, k = map(int, input().split())
    lst = list(map(int, input().rstrip().split()))
    flag = False

    ans = [float('-inf')]
    for i in range(len(lst)):
        if ans[-1] < lst[i]:
            ans.append(lst[i])
        
        ntmp = bisect.bisect_left(ans, lst[i])
        if lst[i] > ans[ntmp - 1] and lst[i] < ans[ntmp]:
            ans[ntmp] = lst[i]
        if len(ans) - 1 >= k:
            flag = True
            break
    
    print("Case #", t + 1, sep="")
    if flag:
        print(1)
    else:
        print(0)