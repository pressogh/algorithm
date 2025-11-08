from itertools import combinations

def solve():
    _, m = map(int, input().split())
    l = filter(lambda x: x < m, map(int, input().split()))

    combi = list(combinations(l, 3))
    res = -1
    for item in combi:
        s = sum(item)
        if s > m:
            continue
        res = max(s, res)

    print(res)

if __name__ == '__main__':
    solve()