"""
You are given an integer n and two arrays each of which is a permutation of numbers from 1 to n.
Your task is to determine the number of unordered triplet (a,b,c) such that 
relative ordering of(a,b,c) is the same in both the arrays

1. combination on list 1 of size 3
2. with combination sets of list1, compare it with the list2

"""

def combination(list1):
    res = []

    def backtrack(path, index):
        if len(path) == 3:
            nonlocal res
            res.append(path[:])
            return
        
        for i in range(index, len(list1)):
            path.append(list1[i])
            backtrack(path, i+1)
            path.pop()

    backtrack([],0)
    print(res)
    return res

def relative_ordering(elem, l2):
    # len(elem) = 3
    i = 0
    for num in l2:
        if num == elem[i]:
            i +=1
            if i == 3:
                return True
    return True if i == 3 else False

def solver(n, l1, l2):
    comb_list = combination(l1)
    res = 0
    for elem in comb_list:
        if relative_ordering(elem,l2):
            res +=1
    return res

print(solver(3,[1,2,3],[1,2,3]))
print(solver(4, [1,2,3,4],[2,1,3,4]))
print(solver(5, [1,2,3,4,5],[2,1,3,4,5]))


