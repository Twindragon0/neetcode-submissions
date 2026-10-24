class ListNode:
    def __init__(self):
        self.val = -1
        self.nxt = None
class MyHashSet:
    
    def __init__(self):
        self.buckets = [ListNode() for _ in range(10000)]
        
    def add(self, key: int) -> None:
        node = self.buckets[key % 10000]
        curr = node
        while curr.nxt != None:
            if curr.nxt.val == key:
                return
            curr = curr.nxt
        curr.nxt = ListNode()
        curr.nxt.val = key
        
    def remove(self, key: int) -> None:
        node = self.buckets[key % 10000]
        prev = node
        curr = node.nxt
        while curr != None:
            if curr.val == key:
                prev.nxt = curr.nxt
                return
            prev = prev.nxt
            curr = curr.nxt
        
    def contains(self, key: int) -> bool:
        node = self.buckets[key % 10000]
        curr = node
        while curr != None:
            if curr.val == key:
                return True
            curr = curr.nxt
        return False
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)