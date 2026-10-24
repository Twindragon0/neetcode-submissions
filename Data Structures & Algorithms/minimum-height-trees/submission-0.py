class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0] * n
        adjList = defaultdict(set)
        for [x, y] in edges:
            indegree[x] += 1
            indegree[y] += 1
            adjList[x].add(y)
            adjList[y].add(x)
        queue = deque()
        toSee = set([i for i in range(n)])
        for i, degree in enumerate(indegree):
            if degree == 1:
                queue.append(i)
        while len(toSee) > 2:
            numToPop = len(queue)
            for i in range(numToPop):
                x = queue.popleft()
                toSee.remove(x)
                for y in adjList[x]:
                    if y not in toSee:
                        continue
                    indegree[y] -= 1
                    indegree[x] -= 1
                    if indegree[y] == 1:
                        queue.append(y)
        return list(toSee)

        