"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ans = Node(0)
        first, second = head, ans
        firstMapping = defaultdict(int)
        secondMapping = defaultdict()
        i = 0
        while first:
            firstMapping[first] = i
            second.next = Node(first.val)
            first, second = first.next, second.next
            secondMapping[i] = second
            i += 1
        
        first, second = head, ans.next
        while second:
            if first.random:
                second.random = secondMapping[firstMapping[first.random]]
            first, second = first.next, second.next
        return ans.next