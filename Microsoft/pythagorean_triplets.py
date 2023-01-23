from collections import defaultdict, deque
"""
https://leetcode.com/discuss/interview-question/2788156/OA-2022-or-Pythagorean-Triplets 

"""

def countPythagoreanTriples(tree_nodes, tree_from, tree_to, x, y, z):
    graph = defaultdict(set)

    for i,j in zip(tree_from, tree_to):
        graph[i].add(j)
        graph[j].add(i)

    dp = {}

    def bfs(cur, target):
        if (cur, target) in dp:
            return dp[(cur, target)]

        visited = {}
        queue = deque()
        queue.append((cur, 0))
        visited[cur] = True

        while queue:
            node, cur_distance = queue.popleft()

            if node == target:
                dp[(node, target)] = cur_distance
                return cur_distance

            if (node, target) in dp:
                return cur_distance + dp[(node, target)]

            if target in graph[node]:
                return cur_distance + 1

            for child in graph[node]:
                if not child in visited:
                    visited[child] = True
                    queue.append((child, cur_distance +1))

    ans = 0

    for node in range(tree_nodes):
        x1 = bfs(node,x)
        x2 = bfs(node,y)

        a, b, c = sorted([x1, x2, bfs(node, z)])

        if a and b and c and a**2 + b**2 == c**2:
            ans +=1

    return ans


