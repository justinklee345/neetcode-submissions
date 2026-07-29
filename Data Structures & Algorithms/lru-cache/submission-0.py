class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.prev, self.next = None, None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.num = 0
        self.LRU, self.MRU = Node(0, 0), Node(0,0)
        self.LRU.next, self.MRU.prev = self.MRU, self.LRU
        self.cache = {}
    
    # insert node to MRU
    def insert(self, node):
        prev = self.MRU.prev
        prev.next = node
        node.prev = prev
        node.next = self.MRU
        self.MRU.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        print("GET", key)
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        print("PUT", key, value)
        if key in self.cache:
            curr = self.cache[key]
            self.remove(curr)
            self.num -= 1
            del curr
        newNode = Node(key, value)
        self.cache[key] = newNode
        self.insert(newNode)
        self.num += 1
        if self.num > self.cap:
            to_remove = self.LRU.next
            print("BRUH")
            print(self.cache)
            print(to_remove.key, to_remove.value)
            ptr = self.LRU
            self.remove(to_remove)
            self.num -= 1
            del self.cache[to_remove.key]
