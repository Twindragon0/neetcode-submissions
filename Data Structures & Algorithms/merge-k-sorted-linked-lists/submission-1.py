# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        curr = ans

        heap = []
        for i, chain in enumerate(lists):
            if chain:
                heapq.heappush(heap, (chain.val, i, chain))
        while heap:
            _, idx, toAdd = heapq.heappop(heap)
            curr.next = toAdd
            curr = curr.next
            lists[idx] = toAdd.next
            if toAdd.next:
                heapq.heappush(heap, (toAdd.next.val, idx, toAdd.next))
        return ans.next