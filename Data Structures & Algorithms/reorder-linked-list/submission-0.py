# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        indices = defaultdict(int)
        
        curr = head
        i = 0
        while curr:
            indices[i] = curr
            curr = curr.next
            indices[i].next = None
            i += 1
        ans = ListNode()
        curr = ans
        i = 0
        n = len(indices.keys())
        while i <= n-1-i:
            if i != n-1-i:
                indices[i].next = indices[n-1-i]
            curr.next = indices[i]
            while curr.next:
                curr = curr.next
            i += 1
        head = ans.next
