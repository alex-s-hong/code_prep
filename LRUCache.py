class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # store key as key, value as Node(key, value)
        self.cache = {}
        # head, tail sentinels for ordering
        self.leastRecent = Node(-1, -1)
        self.mostRecent = Node(-1, -1)
        
        self.leastRecent.next = self.mostRecent
        self.mostRecent.prev = self.leastRecent
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.add(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        new_node = Node(key, value)
        self.cache[key] = new_node
        self.add(new_node)
        if len(self.cache) > self.capacity:
            #self.show()
            del self.cache[self.leastRecent.next.key]
            self.remove(self.leastRecent.next)
            

        
    def remove(self, node):
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev
    
    def add(self, node):
        prev_recent = self.mostRecent.prev
        prev_recent.next = node
        node.prev = prev_recent
        node.next = self.mostRecent
        self.mostRecent.prev = node
        
    def show(self):
        for k,v in self.cache.items():
            print("k: {}, v: {}".format(k,v.val))
        
        mover = self.leastRecent
        while True:
            mover = mover.next
            if mover == self.mostRecent:
                print()
                return
            print(mover.key, mover.val, end= "->")