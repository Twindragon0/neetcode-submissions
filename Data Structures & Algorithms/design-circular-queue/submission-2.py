class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyCircularQueue:

    def __init__(self, k: int):
        self.circularQueue = ListNode()
        self.front = None
        self.back = None

        curr = self.circularQueue
        currK = 1
        while currK < k:
            curr.next = ListNode()
            curr = curr.next
            currK += 1
        curr.next = self.circularQueue

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.circularQueue.val = value
            self.front = self.back = self.circularQueue
        else:
            self.back = self.back.next
            self.back.val = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.front == self.back:
            self.front = self.back = None
        else:
            self.front = self.front.next
        return True

    def Front(self) -> int:
        return self.front.val if self.front else -1

    def Rear(self) -> int:
        return self.back.val if self.back else -1

    def isEmpty(self) -> bool:
        return self.front == None and self.back == None

    def isFull(self) -> bool:
        return not self.isEmpty() and self.back.next == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()