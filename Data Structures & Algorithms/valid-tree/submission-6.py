class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        indegreeList = defaultdict(int)
        adjacencyList = defaultdict(set)
        for edge in edges:
            indegreeList[edge[0]] += 1
            indegreeList[edge[1]] += 1
            adjacencyList[edge[0]].add(edge[1])
            adjacencyList[edge[1]].add(edge[0])
        queue = deque()
        seen = set()
        for i in range(n):
            if indegreeList[i] <= 1:
                queue.append(i)
                seen.add(i)
        while queue:
            node = queue.popleft()
            for x in adjacencyList[node]:
                indegreeList[x] -= 1
                if x not in seen and indegreeList[x] <= 1:
                    queue.append(x)
                    seen.add(x)
        return len(seen) == n
