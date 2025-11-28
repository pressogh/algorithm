import sys, os, io, atexit

input = lambda: sys.stdin.readline().rstrip('\r\n')
stdout = io.BytesIO()
sys.stdout.write = lambda s: stdout.write(s.encode("ascii"))
atexit.register(lambda: os.write(1, stdout.getvalue()))
sys.setrecursionlimit(10 ** 6)

class Node:
    value = None
    left = None
    right = None

    def __init__(self, value):
        self.value = value

class Tree:
    root = None

    def push(self, value):
        node = Node(value=value)
        if self.root is None:
            self.root = node
            return

        tmp = self.root
        parent = self.root
        while parent is not None:
            tmp = parent
            if node.value < parent.value: parent = parent.left
            else: parent = parent.right

        if node.value < tmp.value: tmp.left = node
        else: tmp.right = node
    
    def post(self, node):
        if node is None: return
        self.post(node.left)
        self.post(node.right)
        print(node.value)

tree = Tree()
while True:
    try:
        n = int(input())
        tree.push(n)
    except ValueError:
        break

tree.post(tree.root)
