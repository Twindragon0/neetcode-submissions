"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.map = {}
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        self.map[head] = Node(head.val)
        self.map[head].next = self.copyRandomList(head.next)
        self.map[head].random = self.map[head.random] if head.random else None
        return self.map[head]



        