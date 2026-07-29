class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cnt = 0
        self.cache = {}
        self.LRU, self.MRU = Node(0,0), Node(0,0)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    # insert at MRU
    def insert(self, node):
        # [prev] <-> [MRU]
        prev = self.MRU.prev
        node.prev = prev
        node.next = self.MRU
        prev.next = node
        self.MRU.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.cnt -= 1
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode
        self.cnt += 1
        if self.cnt > self.cap:
            toRemove = self.LRU.next
            self.remove(toRemove)
            del self.cache[toRemove.key]
            self.cnt -= 1

        
