# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        prevLeft = nxt = leftNode = rightNode = None
        i = 1
        curr = head
        while curr:
            if i+1 == left:
                prevLeft = curr
            elif i-1 == right:
                nxt = curr
            elif i == left:
                leftNode = curr
            elif i == right:
                rightNode = curr
            i += 1
            curr = curr.next
        
        curr = leftNode
        prev = nxt
        while curr != nxt:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        if prevLeft:
            prevLeft.next = prev
            return head
        else:
            return prev
        