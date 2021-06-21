from collections import defaultdict, OrderedDict

class Node:
    def __init__(self, key, val, count):
        self.key = key
        self.val = val
        self.count = count


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.minFreq = None
        self.keyToNode = {}
        self.countToNode = defaultdict(OrderedDict) # among countToNode[self.minFreq], pick the oldest


    def get(self, key) -> int:
        if key not in self.keyToNode:
            return -1

        node = self.keyToNode[key]
        # update the freq
        
        del self.countToNode[node.count][key]

        node.count +=1
        self.countToNode[node.count][key] = node

        # check minFreq
        if not self.countToNode[self.minFreq]:
            self.minFreq +=1
        
        return node.val

    
    def put(self, key, value) -> None:
        if not self.capacity:
            return
        
        #update
        if key in self.keyToNode:
            self.keyToNode[key].val = value
            self.get(key) # it will increment its counter

        # insert
        else:
            # capacity reached
            if len(self.keyToNode) == self.capacity:
                key_, _ = self.countToNode[self.minFreq].popitem(last=False)
                print("key {} is deleted".format(key_))
                del self.keyToNode[key_]
            
            self.countToNode[1][key] = self.keyToNode[key] = Node(key, value, 1)
            self.minFreq = 1

cache = LRUCache(2)

cache.put(1,1)
cache.put(2,2)
print(cache.get(1)) # print 1
print(cache.keyToNode)
cache.put(3,3)
print(cache.keyToNode)
print(cache.get(2)) # print -1
print(cache.get(3)) # print 3
cache.put(4,4)
print(cache.get(1)) # print -1
print(cache.get(3)) # print 3
print(cache.get(4)) # print 4

