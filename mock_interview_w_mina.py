"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.

1

4 2

121

1223
"""

print("Hello World")

def isPalindrome(x:int):
    x_list = list(x) ['1','2,''1']
    stack_size= len(x_list) // 2  1
    stack = []

    i = 0

    while i < stack_size:
        stack.append(x_list[i])
        i +=1
        

        #i =1 

    if len(x_list) % 2 != 0:
        i +=1
    
# 
    while i < len(x_list):
        elem = stack.pop()
        if elem != x_list[i]:
            return False
        
        i +=1

    return True

print(isPalindrome(121))


        
