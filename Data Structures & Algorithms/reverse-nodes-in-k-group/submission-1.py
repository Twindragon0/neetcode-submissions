# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        self.ans = head
        def reverseGroup(prevK):
            currK = 0 if prevK else 1
            curr = prevK if prevK else head
            while curr and currK < k:
                curr = curr.next
                currK += 1
            
            if not curr or currK != k:
                return None
            if prevK == None:
                self.ans = curr

            afterK = curr.next
            prevReverse = afterK
            currReverse = prevK.next if prevK else head
            while currReverse != afterK:
                tmp = currReverse.next
                currReverse.next = prevReverse
                prevReverse = currReverse
                currReverse = tmp
            toReturn = prevK.next if prevK else head
            if prevK:
                prevK.next = prevReverse
            return toReturn

        prevK = reverseGroup(None)
        while prevK:
            prevK = reverseGroup(prevK)
        return self.ans
