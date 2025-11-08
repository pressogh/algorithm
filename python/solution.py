def solve():
    n, m = map(int, input().split())
    l = sorted(map(int, input().split()))

    print(n, m)
    print(list(l))

if __name__ == '__main__':
    solve()