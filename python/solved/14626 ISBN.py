def solve():
    n = input()
    checksum = int(n[-1])
    idx = 0
    s = 0
    for i in range(len(n) - 1):
        if n[i] == '*':
            idx = i
            continue

        if i % 2 != 0:
            s += int(n[i]) * 3
        else:
            s += int(n[i])

    for i in range(10):
        ns = s + i * (3 if idx % 2 != 0 else 1)
        nc = 0 if ns % 10 == 0 else 10 - ns % 10
        if nc == checksum:
            print(i)
            break

if __name__ == '__main__':
    solve()