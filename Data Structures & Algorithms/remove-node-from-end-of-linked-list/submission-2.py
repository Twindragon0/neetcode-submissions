# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def recurse(curr):
            if not curr.next:
                return 1
            rest = recurse(curr.next)
            if rest == n:
                curr.next = curr.next.next
            return rest + 1
        num = recurse(head)
        if num == n:
            return head.next
        return head
