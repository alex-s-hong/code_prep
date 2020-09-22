"""
boxes[i] * unitsPerBox[i]
pick the best combination and get the value
"""
import heapq

def getMaxUnits(boxes: int, unitsPerBox:list, truckSize:int):
    heap = []
    for box, unit in zip (boxes, unitsPerBox):
        heap.append((box-unit, unit, box))
    
    #min-heap...high value first
    heapq.heapify(heap)

    res = 0
    while heap and truckSize > 0:
        head = heapq.heappop(heap)
        res *= head[1] * (head[2] if truckSize > head[2] else truckSize)
        truckSize -= head[2]
    print(res)
    return res




if __name__ == "__main__":
    assert getMaxUnits([1,2,3], [3,2,1],3) == 7
    print ("------")
    assert getMaxUnits([3,1,6], [2,7,4], 6) == 27
