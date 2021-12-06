"""
array represenation of binary tree
root:0
root.left = 2*root + 1
root.right = 2*root + 2
parent = (i-1) //2
"""

class MinHeap:

    def __init__(self):
        self.heap = []

    def print(self):
        print(self.heap)

    # zero indexed
    def parentIndex(self, pos):
        return (pos-1) //2
    
    def leftnodeIndex(self,pos):
        return 2*pos+1

    def rightnodeIndex(self,pos):
        return 2*pos+2
    
    def hasLeft(self, pos):
        return self.leftnodeIndex(pos) < len(self.heap)
    
    def hasRight(self, pos):
        return self.rightnodeIndex(pos) < len(self.heap)
    
    def hasParent(self,pos):
        return self.parentIndex(pos) >= 0
    
    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return ValueError
    
    def minimumPop(self):
        if not self.heap:
            return ValueError
        item = self.heap[0]
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap.pop()
        self.heapifyDown()
        return item
    
    def add(self, val):
        self.heap.append(val)
        self.heapifyUp()
    
    def heapifyUp(self):
        index = len(self.heap)-1
        while self.hasParent(index) and self.heap[self.parentIndex(index)] > self.heap[index]:
            self.heap[self.parentIndex(index)], self.heap[index] =  self.heap[index], self.heap[self.parentIndex(index)]
            index = self.parentIndex(index)
        

    def heapifyDown(self):
        index = 0

        while self.hasLeft(index):
            smallerChildIndex = self.leftnodeIndex(index)
            if self.hasRight(index) and self.heap[self.rightnodeIndex(index)] < self.heap[self.leftnodeIndex(index)]:
                    smallerChildIndex = self.rightnodeIndex(index)
            
            if self.heap[index] < self.heap[smallerChildIndex]:
                break
            else:
                self.heap[index], self.heap[smallerChildIndex] = self.heap[smallerChildIndex], self.heap[index]
            index = smallerChildIndex        
    
heap = MinHeap()
heap.add(10)
heap.print()
heap.add(11)
heap.add(5)
heap.add(7)
heap.add(1)
heap.print()
print(heap.peek())
print(heap.minimumPop())
print(heap.minimumPop())
print(heap.minimumPop())
heap.add(2)
print(heap.minimumPop())
heap.print()