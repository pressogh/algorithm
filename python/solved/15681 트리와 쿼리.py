import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

sys.setrecursionlimit(10 ** 6)

n, r, q = map(int, input().split())
connect = [[] for _ in range(n + 1)]
node_parent, node_children = [-1] * (n + 1), [[] for _ in range(n + 1)]
dp = [0] * (n + 1)

def make_tree(current_node, parent):
    for node in connect[current_node]:
        if node == parent: continue

        node_children[current_node].append(node)
        node_parent[node] = current_node
        make_tree(node, current_node)


def count_sub_tree_nodes(current_node):
    dp[current_node] = 1
    for node in node_children[current_node]:
        count_sub_tree_nodes(node)
        dp[current_node] += dp[node]


for _ in range(n - 1):
    u, v = map(int, input().split())
    connect[u].append(v)
    connect[v].append(u)

make_tree(r, -1)
count_sub_tree_nodes(r)

while q > 0:
    q -= 1
    print(dp[int(input())])