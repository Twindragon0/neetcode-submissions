class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.mappings = defaultdict()
        self.head = None
        self.tail = None
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.mappings:
            self.updateKey(key)
            return self.mappings[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.mappings:
            self.mappings[key].val = value
            self.updateKey(key)
        else:
            self.mappings[key] = ListNode(key, value, None, self.tail)
            if self.tail:
                self.tail.next = self.mappings[key]
                self.tail = self.tail.next
            else:
                self.head = self.tail = self.mappings[key]

            # prune list if too big
            if len(self.mappings.keys()) > self.capacity:
                self.mappings.pop(self.head.key)
                self.head = self.head.next
                self.head.prev = None
    
    def updateKey(self, key):
        if self.mappings[key] != self.tail:
            prevNode = self.mappings[key].prev
            if prevNode:
                prevNode.next = self.mappings[key].next
                prevNode.next.prev = prevNode
            else:
                self.head = self.head.next
                self.mappings[key].next.prev = None
            self.mappings[key].next = None
            self.mappings[key].prev = self.tail
            self.tail.next = self.mappings[key]
            self.tail = self.tail.next


        
        
        
