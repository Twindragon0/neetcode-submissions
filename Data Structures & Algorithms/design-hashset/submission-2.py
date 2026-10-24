class ListNode:
    def __init__(self):
        self.val = -1
        self.nxt = None
class MyHashSet:
    
    def __init__(self):
        self.buckets = [0] * 31251
        
    def add(self, key: int) -> None:
        self.buckets[key // 32] = self.buckets[key // 32] | (1 << key % 32)
        
    def remove(self, key: int) -> None:
        self.buckets[key // 32] = self.buckets[key // 32] & ~(1 << key % 32)
        
    def contains(self, key: int) -> bool:
        val = self.buckets[key // 32] | ~(1 << key % 32)
        # if all 1s, it means we need to return True
        if ~val == 0:
            return True
        else:
            return False


        
        

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)