# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans
        carryOn = 0
        while l1 or l2:
            nextVal = 0
            if l1:
                nextVal += l1.val
                l1 = l1.next
            if l2:
                nextVal += l2.val
                l2 = l2.next
            curr.next = ListNode((nextVal + carryOn) % 10)
            carryOn = (nextVal + carryOn) // 10
            curr = curr.next
        if carryOn == 1:
            curr.next = ListNode(1)
        return ans.next

        