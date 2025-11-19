import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

graph = []
res = set()

def recursive(node):
    global graph, res
    res.add(node)

    if len(graph[node]) == 0:
        return
    
    for item in graph[node]:
        if item not in res:
            recursive(item)

def solve():
    n, m = int(input()), int(input())
    global graph
    graph = [set() for _ in range(n + 1)]
    for _ in range(m):
        c1, c2 = map(int, input().split())
        graph[c1].add(c2)
        graph[c2].add(c1)
    
    recursive(1)
    print(len(res) - 1)

if __name__ == '__main__':
    solve()