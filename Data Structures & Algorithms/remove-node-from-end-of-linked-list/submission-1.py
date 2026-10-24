# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = right = head
        curr = 0
        while right.next and curr < n:
            curr += 1
            right = right.next
        if curr < n:
            return head.next
        while right.next:
            right = right.next
            left = left.next
        left.next = left.next.next
        return head