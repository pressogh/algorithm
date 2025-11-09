def solve():
    l = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]]
    for _ in range(14):
        a = []
        for j in range(len(l[0])):
            a.append(l[-1][j] + a[-1] if j > 0 else l[-1][j])
        l.append(a)

    t = int(input())

    for _ in range(t):
        k = int(input())
        n = int(input())
        print(l[k][n - 1])
        
if __name__ == '__main__':
    solve()