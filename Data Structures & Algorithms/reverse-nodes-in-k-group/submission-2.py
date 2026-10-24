# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        currK = 1
        curr = head
        while curr and currK < k:
            curr = curr.next
            currK += 1
        if currK < k or not curr:
            return head
        nextHead = self.reverseKGroup(curr.next, k)
        prevNode = nextHead
        currNode = head
        while prevNode != curr:
            tmp = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = tmp
        return curr