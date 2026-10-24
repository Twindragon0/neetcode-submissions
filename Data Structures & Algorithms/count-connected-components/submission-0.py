class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(set)
        for [x, y] in edges:
            adjList[x].add(y)
            adjList[y].add(x)
        
        visited = set()
        ans = 0
        for i in range(n):
            if i in visited:
                continue
            visited.add(i)
            queue = deque()
            queue.append(i)
            while queue:
                x = queue.popleft()
                for y in adjList[x]:
                    if y in visited:
                        continue
                    visited.add(y)
                    queue.append(y)
                    adjList[y].remove(x)
            ans += 1
        return ans  