class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        seen = set()
        adjList = defaultdict(set)
        indegreeList = defaultdict(int)
        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])
            indegreeList[edge[0]] += 1
            indegreeList[edge[1]] += 1
        queue = deque()
        for i in range(n):
            if indegreeList[i] <= 1:
                seen.add(i)
                queue.append(i)
        while queue:
            size = len(queue)
            ans = []
            for i in range(size):
                x = queue.popleft()
                ans.append(x)
                for y in adjList[x]:
                    indegreeList[y] -= 1
                    if y not in seen and indegreeList[y] == 1:
                        seen.add(y)
                        queue.append(y)
        return ans