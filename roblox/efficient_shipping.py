"""
boxes[i] * unitsPerBox[i]
pick the best combination and get the value
"""
import heapq

def getMaxUnits(boxes: int, unitsPerBox:list, truckSize:int):
    heap = []
    for box, price in zip (boxes, unitsPerBox):
        heap.append((-price, box))
    
    #min-heap...high unitPrice first as sign reverted
    heapq.heapify(heap)

    res = 0
    while heap and truckSize > 0:
        price, box = heapq.heappop(heap)
        price = -price
        res += price * (box if truckSize > box else truckSize)
        truckSize -= box
    return res




if __name__ == "__main__":
    assert getMaxUnits([1,2,3], [3,2,1],3) == 7
    assert getMaxUnits([3,1,6], [2,7,4], 6) == 27
    assert getMaxUnits([1],[2], 1) == 2

