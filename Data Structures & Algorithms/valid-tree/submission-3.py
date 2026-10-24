class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adjList = defaultdict(set)
        for [x, y] in edges:
            adjList[x].add(y)
            adjList[y].add(x)
        queue = deque()
        visited.add(0)
        queue.append(0)
        while queue:
            x = queue.popleft()
            for y in adjList[x]:
                if y in visited:
                    return False
                adjList[y].remove(x)
                visited.add(y)
                queue.append(y)
        return len(visited) == n