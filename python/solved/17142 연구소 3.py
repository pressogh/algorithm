# 17142
import collections          # 가장 많은 숫자, deque 등
import sys                  # 여러줄 입력
import itertools            # 순열 조합(permutations, combinations)
input = sys.stdin.readline

def prettyPrint(arr):
    for i in range(n):
        for j in range(n):
            print(arr[i][j], end='\t')
        print()


n, m = map(int, input().rstrip().split())
lst = [list(map(int, input().rstrip().split())) for _ in range(n)]

# * 연산자로 배열 만들 시 오류 있음
ans = [[float('inf') for _ in range(n)] for _ in range(n)]

def isSafe(x, y):
    return 0 <= x < n and 0 <= y < n

def getMax(arr):
    max = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] != '-' and arr[i][j] != '*':
                if arr[i][j] > max:
                    max = arr[i][j]
    return max

q = collections.deque()
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

exp = []
def bfs():
    while q:
        tmp = q.popleft()
        for i in range(4):
            nx = tmp[0] + dx[i]
            ny = tmp[1] + dy[i]

            if isSafe(nx, ny):
                if ans[nx][ny] == float('inf'):
                    ans[nx][ny] = ans[tmp[0]][tmp[1]] + 1
                    q.append((nx, ny))
                if ans[nx][ny] == '*':
                    ans[nx][ny] = ans[tmp[0]][tmp[1]] + 1
                    exp.append((nx, ny))
                    q.append((nx, ny))

tmp = []
zeroidx = []
virusidx = []
for i in range(len(lst)):
    for j in range(len(lst[i])):
        if lst[i][j] == 2:
            ans[i][j] = '*'
            virusidx.append((i, j))
            tmp.append((i, j))
        elif lst[i][j] == 1:
            ans[i][j] = '-'
        elif lst[i][j] == 0:
            zeroidx.append((i, j))

comb = list(itertools.combinations(tmp, m))

ansnum = float('inf')
for coor in comb:
    for item in coor:
        q.append(item)
        ans[item[0]][item[1]] = 0
    bfs()

    for item in exp:
        ans[item[0]][item[1]] = 0
    exp.clear()

    if getMax(ans) < ansnum:
        ansnum = getMax(ans)

    for item in zeroidx:
        ans[item[0]][item[1]] = float('inf')
    for item in virusidx:
        ans[item[0]][item[1]] = '*'

if ansnum == float('inf'):
    print(-1)
else:
    print(ansnum)