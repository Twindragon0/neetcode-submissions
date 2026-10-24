class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyCircularQueue:

    def __init__(self, k: int):
        self.size = 0
        self.k = k

        head = ListNode(0)
        curr = head
        i = 1
        while i != k:
            curr.next = ListNode(0)
            curr = curr.next
            i += 1
        curr.next = head

        self.front = head
        self.rear = head

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.size != 0:
            self.rear = self.rear.next
        else:
            self.front = self.rear
        self.rear.val = value
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.front = self.front.next
        self.size -= 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.front.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.rear.val
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()