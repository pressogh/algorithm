def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solve():
    n, m = map(int, input().split())
    g = gcd(n, m)
    print(g, n * m // g, sep = '\n')

if __name__ == '__main__':
    solve()