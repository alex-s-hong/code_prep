#! usr/bin/env/python3

import os
import sys
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return "Node with {}".format(self.val)


def build_tree(indexes):
    f = lambda x: None if x == -1 else Node(x)
    # children : merely a transformation to node representation
    children = [list(map(f,x)) for x in indexes]
    # print ("children", children)
    nodes = {n.val: n for n in filter(None, sum(children, []))} # what is sum(children, [])?
    print (nodes)
    nodes[1] = Node(1)
    for idx, child_pair in enumerate(children):
        nodes[idx+1].left = child_pair[0]
        nodes[idx+1].right = child_pair[1]
    return nodes[1]

def inorder(root):
    stack = []
    curr = root
    while stack or curr:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            curr = stack.pop()
            yield curr.val
            curr = curr.right

def swapNodes(indexes: list, queries: list):
    """
    indexes comes in from root's first children, from left to right bfs style, 
    queries: Given a tree and an integer, k, in one operation, 
    we need to swap the subtrees of all the nodes at each depth h, where h ∈ [k, 2k, 3k,...].
    """
    #print(indexes)
    #print(queries)
    root = build_tree(indexes)
    for k in queries:
        h = 1
        q = deque([root])
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if h % k == 0:
                    node.left, node.right = node.right, node.left
                q += filter(None, (node.left, node.right))
            h += 1
        return inorder(root)

    
if __name__ == '__main__':
    i0 = [[2, 3], [-1, -1], [-1, -1]]
    q0 = [1, 1]

    i1 = [[2, 3], [4, 5], [6, -1], [-1, 7], [8, 9], [10, 11], [12, 13], \
         [-1, 14], [-1, -1], [15, -1], [16, 17], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1]]
    q1 = [2, 3]

    i2 = [[2, 3], [4, -1], [5, -1], [6, -1], [7, 8], [-1, 9], [-1, -1], [10, 11], [-1, -1], [-1, -1], [-1, -1]]
    q2 = [2, 4]

    print("case 0")
    r0 = swapNodes(i0, q0)
    print(*r0)

    print("case 1")
    r1 = swapNodes(i1, q1)
    print(*r1)

    print("case 2")
    #r2 = swapNodes(i2, q2)
    #print(*r2)