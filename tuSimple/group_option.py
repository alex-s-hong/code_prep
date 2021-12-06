"""
return the number of combinations of m that sums to n where element of each group should be non decreasing order
n = 8
m = 4
output = 5
explanation:
[1,1,1,5], [1,1,2,4],[1,1,3,3],[1,2,2,3],[2,2,2,2]

"""

def group_option(m, n):
    if n < m:
        return 0
    res = 0

    def backtrack(path, cur_elem, remain):
        if remain == 0 and len(path) == m:
            nonlocal res
            res += 1
            return
        elif remain < 0 or len(path) == m:
            return
        else:
            for i in range(cur_elem, remain+1):
                path.append(i)
                backtrack(path, i, remain-i)
                path.pop()
    
    backtrack([],1, n)

    return res

print(group_option(4,8))
print(group_option(5,7))


