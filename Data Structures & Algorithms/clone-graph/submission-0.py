"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        ans = Node(node.val)
        visited = defaultdict(Node)
        visited[node.val] = ans
        queue = deque()
        queue.append((ans, node))
        while queue:
            new, prev = queue.popleft()
            for child in prev.neighbors:
                if child.val in visited:
                    new.neighbors.append(visited[child.val])
                else:
                    visited[child.val] = Node(child.val)
                    queue.append((visited[child.val], child))
                    new.neighbors.append(visited[child.val])
        return ans