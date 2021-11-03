class node():
    def __init__(self):
        self.parents = None
        self.child = []


node_num = int(input())
info = list(map(int, input().split()))
del_node_num = int(input())

tree = [0] * node_num
for i in range(node_num):
    if tree[i] == 0:
        tree[i] = node()
    tree[i].parents = info[i]

    if tree[info[i]] == 0:
        tree[info[i]] = node()

    if info[i] == -1:
        root = i
    else:
        tree[info[i]].child.append(i)

leaf = 0

if tree[del_node_num].parents != -1:  # root node가 아닌경우
    tree[tree[del_node_num].parents].child.remove(del_node_num)  # del node link
else:
    tree[del_node_num].child = []
    leaf = -1

q = tree[root].child

while q:
    Next = []
    for v in q:
        if len(tree[v].child) == 0:
            leaf += 1
        for u in tree[v].child:
            Next.append(u)
    q = Next
if leaf == -1:
    print(leaf + 1)
elif leaf == 0:
    print(1)
else:
    print(leaf)