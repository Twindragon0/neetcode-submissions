class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjList = defaultdict(set)
        indegree = [0] * max(max(edge[0], edge[1]) for edge in edges)
        for [start, end] in edges:
            adjList[start].add(end)
            adjList[end].add(start)
            indegree[end-1] += 1
            indegree[start-1] += 1
        queue = deque()
        for i in range(len(indegree)):
            if indegree[i] == 1:
                queue.append(i+1)
        while queue:
            x = queue.popleft()
            for y in adjList[x]:
                indegree[x-1] -= 1
                indegree[y-1] -= 1
                if indegree[y-1] == 1:
                    queue.append(y)
        for edge in reversed(edges):
            if indegree[edge[0]-1] > 1 and indegree[edge[1]-1] > 1:
                return edge

        
