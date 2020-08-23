"""
You are asked to cut off all the trees in this forest in the order of tree's height 
- always cut off the tree with lowest height first. And after cutting, 
the original place has the tree will become a grass (value 1).

You will start from the point (0, 0) and you should output the minimum steps 
you need to walk to cut off all the trees. If you can't cut off all the trees, 
output -1 in that situation.

You are guaranteed that no two trees have the same height and there is at least 
one tree needs to be cut off.
"""

class Solution:
    def cutOffTree(self, forest: list) -> int:
        
        rows = len(forest)
        cols = len(forest[0])
        
        # why do we do this padding?
        forest.append([0] * cols)
        for row in forest:
        	row.append(0)

        trees = {(i,j) for i in range(rows) for j in range(cols) if forest[i][j] >1}

        # initialize reachable path with starting point (0,0)
        reachables = {(0,0)}
        stack = [(0,0)] # why stack, not queue?
        while stack:
        	i, j = stack.pop()
        	for x, y in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
        		if forest[x][y] != 0 and (x,y) not in reachables:
        			reachables.add((x,y))
        			stack.append((x,y))

        # check whether there is any unreachable tree
        if trees.difference(reachables):
        	return -1

        trees = sorted(trees, key= lambda x: forest[x[0]][x[1]])
        if trees[0] != (0, 0):
        	#starting point should be guaranteed to be in the list
        	trees.insert(0, (0,0))

        def shortest_path(node1, node2):
        	estimate = abs(node1[0] - node2[0]) + abs(node2[1] - node2[1])
        	stack1, stack2 = [node1], []
        	used, visited = {node1}, {node1}

        	while True:
        		if not stack1:
        			stack1, stack2 = stack2, stack1
        			used.update(stack1)
        			estimate += 2

        		p = stack1.pop()
        		if p == node2:
        			break

        		i, j = p
        		add1, add2 = [], [] # what is this?

        		if i == node2[0]:
        			add2.append((i-1, j))
        			add2.append((i+1, j))

        		elif i < node2[0]:
                    add2.append((i - 1, j))
                    add1.append((i + 1, j))
                else:
                    add1.append((i - 1, j))
                    add2.append((i + 1, j))

                if j == node2[1]:
                    add2.append((i, j - 1))
                    add2.append((i, j + 1))
                elif j < node2[1]:
                    add2.append((i, j - 1))
                    add1.append((i, j + 1))
                else:
                    add1.append((i, j - 1))
                    add2.append((i, j + 1))

                for v in add1:
                    if forest[v[0]][v[1]] != 0 and v not in used:
                        visited.add(v)
                        used.add(v)
                        stack1.append(v)
                for v in add2:
                    if forest[v[0]][v[1]] != 0 and v not in visited:
                        visited.add(v)
                        stack2.append(v)

            return estimate


        return sum(shortest_path(trees[i-1], trees[i]) for i in range(1, len(trees)))
