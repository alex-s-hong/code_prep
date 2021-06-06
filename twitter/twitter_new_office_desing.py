"""
https://leetcode.com/discuss/interview-question/373110/Twitter-or-OA-2019-or-New-Office-Design

tablePositions, tableHeights

if there is a gap between table, we can place hashtags but the height cannot exceed 
surrounding table + 1, (minHeight(adj)+1)

find the maximum height of hashtag

"""

def getHeight(lp, rp, lh, rh):
    shortH, tallH = min(lh, rh), max(lh, rh)

    gap = abs(lp-rp)-1

    if tallH < shortH+gap:
        return shortH + gap
    
    else:
        diff = tallH-shortH
        gap = gap - diff
        return (tallH+gap) // 2 if gap %2 == 0 else (tallH+gap) // 2 + 1

def maxHeight(tablePositions, tableHeights):
    taux = list(sorted(zip(tablePositions, tableHeights), key= lambda x: x[0]))
    print(taux)
    maxheight = 0
    for i in range(1, len(tablePositions)):
        if abs(tablePositions[i-1]-tablePositions[i])> 1:
            # gap detected
            maxheight = max(maxheight, getHeight(tablePositions[i-1], tablePositions[i], tableHeights[i-1], tableHeights[i]))
        
    return maxheight


print(maxHeight([1,2,4,7],[4,5,7,11]))
print(maxHeight([2,1,10],[2,1,5]))
print(maxHeight([3,1,3,7],[3,4,3,3]))
print(maxHeight([1,2], [1,5]))