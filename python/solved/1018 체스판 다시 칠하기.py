import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

w_start_board = "WBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBW"
b_start_board = "BWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWBBWBWBWBWWBWBWBWB"

def solve():
    n, m = map(int, input().split())
    c = []
    for _ in range(n):
        c.append(input())
    
    res = 64
    for l in range(n - 8 + 1):
        for k in range(m - 8 + 1):
            s = ""
            for i in range(8):
                s += c[i + l][k : k + 8]
            
            r1, r2 = 0, 0
            for i in range(64):
                if s[i] != w_start_board[i]:
                    r1 += 1
                if s[i] != b_start_board[i]:
                    r2 += 1
            res = min(res, min(r1, r2))
    print(res)

if __name__ == '__main__':
    solve()