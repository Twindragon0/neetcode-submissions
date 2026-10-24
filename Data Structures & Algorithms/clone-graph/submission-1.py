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
        def dfs(curr, prev):
            for neighbor in prev.neighbors:
                if neighbor.val in visited:
                    curr.neighbors.append(visited[neighbor.val])
                else:
                    visited[neighbor.val] = Node(neighbor.val)
                    dfs(visited[neighbor.val], neighbor)
                    curr.neighbors.append(visited[neighbor.val])
        dfs(ans, node)
        return ans
