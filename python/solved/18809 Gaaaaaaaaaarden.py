# 18809
import collections          # 가장 많은 숫자, deque 등
import sys                  # 여러줄 입력
import itertools            # 순열 조합(permutations, combinations)
input = sys.stdin.readline

n, m = 0, 0

def isSafe(x, y):
    return 0 <= x < n and 0 <= y < m

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(lst, g, r):
    q = collections.deque()
    check = [[[-1, ''] for _ in range(m)] for _ in range(n)]

    for item in g:
        coor = list(item)
        q.append([coor[0], coor[1]])
        check[coor[0]][coor[1]][0] = 0
        check[coor[0]][coor[1]][1] = 'g'
    for item in r:
        coor = list(item)
        q.append([coor[0], coor[1]])
        check[coor[0]][coor[1]][0] = 0
        check[coor[0]][coor[1]][1] = 'r'

    while q:
        x, y = q[0]
        q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if isSafe(nx, ny) and lst[nx][ny] != 0 and check[x][y][1] != 'f':
                if check[nx][ny][0] == check[x][y][0] + 1 and ((check[nx][ny][1] == 'r' and check[x][y][1] == 'g') or (check[nx][ny][1] == 'g' and check[x][y][1] == 'r')):
                    check[nx][ny][1] = 'f'
                    continue
                if check[nx][ny][0] == -1:
                    check[nx][ny][0] = check[x][y][0] + 1
                    check[nx][ny][1] = check[x][y][1]
                    q.append([nx, ny])

    tans = 0
    for i in range(n):
        for j in range(m):
            if check[i][j][1] == 'f':
                tans += 1
    return tans

# 0: 호수, 1: 그냥 땅, 2: 배양액을 뿌릴 수 있는 땅
n, m, g, r = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(n)]

ground = []
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == 2:
            ground.append((i, j))


ans = 0
ground = set(ground)
for green in itertools.combinations(ground, r=g):
    red_ground = list(ground - set(green))
    for red in itertools.combinations(red_ground, r=r):
        res = bfs(arr, list(green), list(red))
        if res > ans:
            ans = res


# bfs(arr, ((4, 1), (3, 2)), ((3, 0), (2, 2)))

print(ans)