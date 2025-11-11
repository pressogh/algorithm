def solve():
    n = int(input())

    t = 1
    while True:
        if "666" in str(t):
            n -= 1
            if n <= 0:
                print(t)
                return
        t += 1

if __name__ == '__main__':
    solve()