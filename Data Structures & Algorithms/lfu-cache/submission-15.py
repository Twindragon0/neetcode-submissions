class ListNode:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = prev
        self.next = next
class LFUCache:

    def __init__(self, capacity: int):
        self.frequencyMap = defaultdict() # frequency->[head, tail]
        self.capacity = capacity
        self.keyToNode = defaultdict() # key->ListNode
        self.lowestFreq = 0

    def get(self, key: int) -> int:
        if key in self.keyToNode:
            self.updateFreq(key)
            # print("get: " + str(self.lowestFreq) + " head: " + str(self.frequencyMap[self.lowestFreq][0].key) + " tail: " + str(self.frequencyMap[self.lowestFreq][1].key))
            return self.keyToNode[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyToNode:
            self.keyToNode[key].val = value
            self.updateFreq(key)
        else:
            if self.capacity == 0:
                nodeToEvict = self.frequencyMap[self.lowestFreq][0]
                if not nodeToEvict.next:
                    self.frequencyMap.pop(self.lowestFreq)
                else:
                    self.frequencyMap[self.lowestFreq][0] = nodeToEvict.next
                    nodeToEvict.next.prev = None
                self.keyToNode.pop(nodeToEvict.key)
                self.capacity += 1
            # add the node
            self.keyToNode[key] = ListNode(key, value)
            self.addToEnd(1, self.keyToNode[key])
            # print("put: " + str(self.lowestFreq) + " head: " + str(self.frequencyMap[self.lowestFreq][0].key) + " tail: " + str(self.frequencyMap[self.lowestFreq][1].key))

    def addToEnd(self, frequency, node):
        node.freq = frequency
        self.lowestFreq = 1 if self.lowestFreq == 0 else min(self.lowestFreq, node.freq)
        if frequency not in self.frequencyMap:
            self.frequencyMap[frequency] = [node, node]
        else:
            node.prev = self.frequencyMap[frequency][1]
            node.next = None
            self.frequencyMap[frequency][1].next = node
            self.frequencyMap[frequency][1] = node
        self.capacity -= 1

    def updateFreq(self, key):
        node = self.keyToNode[key]
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.prev:
            node.prev.next = None
            self.frequencyMap[node.freq][1] = node.prev
        elif node.next:
            node.next.prev = None
            self.frequencyMap[node.freq][0] = node.next
        else:
            self.frequencyMap.pop(node.freq)
            if self.lowestFreq == node.freq:
                self.lowestFreq += 1
        self.capacity += 1
        self.addToEnd(node.freq + 1, node)

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)