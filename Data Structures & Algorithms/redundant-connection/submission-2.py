class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(set)
        indegree = defaultdict(int)
        for [x, y] in edges:
            indegree[x] += 1
            indegree[y] += 1
            adjList[x].add(y)
            adjList[y].add(x)
        queue = deque()
        for x in indegree.keys():
            if indegree[x] == 1:
                queue.append(x)
        while queue:
            x = queue.popleft()
            indegree[x] -= 1
            for y in adjList[x]:
                adjList[y].remove(x)
                indegree[y] -= 1
                if indegree[y] == 1:
                    queue.append(y)
            adjList[x] = set()
        for [x, y] in reversed(edges):
            if indegree[x] > 1 and indegree[y] > 1:
                return [x, y]
        return [0,0]