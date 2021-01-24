#! usr/bin/env python3

"""
https://leetcode.com/discuss/interview-question/424737/photo-album-problem

solve with Linked List, not stack
"""

def photo_album(n:int, index:list, identity:list)->list:
    stack1, stack2 = [], []
    for i in range(n):
        while len(stack1) > index[i]:
            stack2.append(stack1.pop())
        stack1.append(identity[i])

        while stack2:
            stack1.append(stack2.pop())

    while stack2:
        stack1.append(stack2.pop())
    return stack1

#print(photo_album(5, [0,1,2,1,2], [0,1,2,3,4]))

#print(photo_album(5, [0,1,2,3,4], [0,1,2,3,4]))
#print(photo_album(5, [0,1,2,4,3], [0,1,2,3,4]))
print(photo_album(7, [0,1,2,3,1,3,6], [0,1,2,3,4,5,6]))