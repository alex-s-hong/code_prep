"""
camera_unobservation_scope
[[15,30],[10,20],[0,3]]

"""

def solver(L:int, cameras_scope:list)-> int:
    if not cameras_scope or L == 0:
        return L
    
    cameras_scope.sort(key=lambda x: x[0])

    res = L
    tmp = []

    for scope in cameras_scope:
        if not tmp or tmp[-1][1] < scope[0]:
            tmp.append(scope)
        else:
            tmp[-1][1] = max(tmp[-1][1], scope[1])
    
    for elem in tmp:
        res -= elem[1]-elem[0]
    
    return res

    

assert solver(50,[[15,30],[10,20],[0,3]]) == 27
assert solver(50,[[15,30],[10,20],[1,3]]) == 28
assert solver(10,[[3,5],[3,7]]) == 6
assert solver(0,[[15,30],[10,20],[0,3]]) == 0
print(solver(30, [[1,3],[2,6],[8,10],[15,18]]))