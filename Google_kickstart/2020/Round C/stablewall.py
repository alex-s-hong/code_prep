#! /usr/bin/env python3

# from collections import defaultdict, deque

# """
# A polyomino is supported if each of its squares is either on the ground, or has another square below it.
# """
# T = int(input())

# for i in range(1, T+1):
#     topological = defaultdict(list) # parent: children
#     visited = defaultdict(bool)
#     res = ''
#     R, C = map(int, input().split())
#     board = []
#     descendents = set()
#     board.append(list(input()))
#     for j in range(1,R):
#         board.append(list(input()))
#         for k in range(len(board[j])):
#             if board[j-1][k] != board[j][k] and board[j-1][k] not in topological[board[j][k]]:
#                 topological[board[j][k]].append(board[j-1][k])
#                 descendents.add(board[j-1][k])
#                 if board[j][k] in topological[board[j-1][k]] and board[j-1][k] in topological[board[j][k]]:
#                     res = -1

#             if j == R-1:
#                 topological[board[j][k]]
    
#     # dfs
#     # start with node that has no incoming nodes
#     # if whole keys is subset of des : cycle!
    
#     init = set(topological.keys()).difference(descendents)
#     # if i >=4:
#     #     print("topo", topological)
#     #     print("des", descendents)
#     #     print("init", init)

#     if res ==-1 or not init:
#         res = -1
#     else:
#         # no cycle
#         stack = []
#         def dfs(node, stack):
#             visited[node] = True

#             for child in topological[node]:
#                 if not visited[child]:
#                     dfs(child, stack)
            
#             stack.append(node)

    
#         for elem in init:
#             if not visited[elem]:
#                 dfs(elem, stack)


#         res = "".join(stack[::-1])
            
#     print("Case #{}: {}".format(i, res))

from collections import *
import sys
try: inp = raw_input
except: inp = input

def err(s):
    sys.stderr.write('{}\n'.format(s))

def ni():
    return int(inp())

def nl():
    return [int(_) for _ in inp().split()]

def out(t, ans):
    print('Case #{}: {}'.format(t, ans))

def solve(G):
    R, C = len(G), len(G[0])
    figs = set(''.join(''.join(l) for l in G))
    used = []
    while figs:
        found = False
        for c in figs:
            fail = False
            for x in range(R-1):
                for y in range(C):
                    if G[x][y] == c:
                        if G[x+1][y] != c and G[x+1][y] not in used:
                            fail = True
                            break
            if not fail:
                found = True
                figs.remove(c)
                used.append(c)
                break
        if not found:
            return '-1'
    return ''.join(used)

T = ni()
for t in range(1, T+1):
    R, C = nl()
    G = [list(inp()) for _ in range(R)]
    ans = solve(G)
    out(t, ans)