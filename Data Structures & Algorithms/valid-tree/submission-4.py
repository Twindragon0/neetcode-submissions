class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        visited = set()
        adjList = defaultdict(set)
        for [x, y] in edges:
            adjList[x].add(y)
            adjList[y].add(x)
        def dfs(x):
            for y in adjList[x]:
                if y in visited:
                    return False
                adjList[y].remove(x)
                visited.add(y)
                dfs(y)
            return True
        visited.add(0)
        return False if not dfs(0) else len(visited) == n