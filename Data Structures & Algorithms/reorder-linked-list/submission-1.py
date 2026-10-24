# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        def recurse(first, last):
            if not last:
                return first
            
            newFirst = recurse(first, last.next)
            if not newFirst:
                return None
            if newFirst != last and newFirst.next != last:
                tmp = newFirst.next
                newFirst.next = last
                last.next = tmp
                return tmp
            else:
                last.next = None
                return None

        recurse(head, head.next)