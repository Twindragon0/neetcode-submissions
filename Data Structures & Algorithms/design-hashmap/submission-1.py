class ListNode:
    def __init__(self):
        self.key = None
        self.val = None
        self.nxt = None

class MyHashMap:
    def __init__(self):
        self.buckets = [ListNode() for _ in range(10000)]
        
    def put(self, key: int, value: int) -> None:
        node = self.buckets[key // 10000]
        curr = node
        while curr.nxt != None:
            if curr.nxt.key == key:
                curr.nxt.val = value
                return
            curr = curr.nxt
        curr.nxt = ListNode()
        curr.nxt.key = key
        curr.nxt.val = value
        
    def get(self, key: int) -> int:
        node = self.buckets[key // 10000]
        curr = node
        while curr != None:
            if curr.key == key:
                return curr.val
            curr = curr.nxt
        return -1
        
    def remove(self, key: int) -> None:
        node = self.buckets[key // 10000]
        prev = node
        curr = node.nxt
        while curr != None:
            if curr.key == key:
                prev.nxt = curr.nxt
                return
            prev = prev.nxt
            curr = curr.nxt


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)