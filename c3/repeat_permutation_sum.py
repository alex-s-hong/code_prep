# find all the combinations of a positive integer with 123
# 3 is [1,1,1], [1,2], [2,1], [3] order matters
# 4 is 1 + 3, 1 + 1 + 2, ...
# reusable, make all combinations to make the number (target)

def combpermuSum(digits:list, target:int):
    result = []

    def backtrack(remain, comb):
        if remain == 0:
            result.append(comb[:])
        
        elif remain < 0:
            return
        
        else:
            for i in range(len(digits)):
                
                comb.append(digits[i])

                backtrack(remain-digits[i], comb)

                comb.pop()
        
    backtrack(target, [])

    return result

print(combpermuSum([1,2,3],3))