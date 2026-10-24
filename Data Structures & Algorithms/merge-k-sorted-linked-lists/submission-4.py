# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def divide(left, right):
            if left > right:
                return None
            if left == right:
                return lists[left]
            mid = (left + right) // 2
            list1 = divide(left, mid)
            list2 = divide(mid+1, right)
            return conquer(list1, list2)

        def conquer(list1, list2):
            ans = ListNode()
            curr = ans
            head1 = list1
            head2 = list2
            while head1 or head2:
                if head1 and head2 and head1.val <= head2.val:
                    curr.next = head1
                    head1 = head1.next
                elif head1 and head2:
                    curr.next = head2
                    head2 = head2.next
                elif head1:
                    curr.next = head1
                    head1 = head1.next
                else:
                    curr.next = head2
                    head2 = head2.next
                curr = curr.next
            return ans.next
        return divide(0, len(lists)-1)

