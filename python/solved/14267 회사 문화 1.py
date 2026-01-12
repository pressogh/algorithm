import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

tree = [[] for _ in range(n)]
for curr_node, parent in enumerate(map(lambda x: int(x) - 1, input().split()[1:]), start=1):
    tree[parent].append(curr_node)
    tree[curr_node].append(parent)

v = [0] * n
for _ in range(m):
    i, w = map(int, input().split())
    v[i - 1] += w

node_parent, node_children, dp = [-1] * n, [[] for _ in range(n)], [0] * n


def make_tree(current_node, parent):
    for node in tree[current_node]:
        if node == parent: continue

        node_children[current_node].append(node)
        node_parent[node] = current_node
        make_tree(node, current_node)


def calc(current_node):
    dp[current_node] += v[current_node]
    for node in node_children[current_node]:
        dp[node] += dp[current_node]
        calc(node)


make_tree(0, -1)
calc(0)

print(*dp)