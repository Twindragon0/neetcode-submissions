# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans
        
        first = list1
        second = list2
        while first or second:
            toUse = None
            if first and second and first.val <= second.val:
                toUse = first
                first = first.next
            elif first and second:
                toUse = second
                second = second.next
            elif first:
                toUse = first
                first = first.next
            else:
                toUse = second
                second = second.next
            curr.next = toUse
            curr = curr.next
        return ans.next
