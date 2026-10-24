# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        i = 0
        curr = head
        if size-n-1 == -1:
            return head.next
        while i != size-n-1:
            i += 1
            curr = curr.next
        curr.next = curr.next.next
        return head