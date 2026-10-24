class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adjList = defaultdict(set)
        for i, [x, y] in enumerate(equations):
            adjList[x].add((y, values[i]))
            adjList[y].add((x, 1/values[i]))
        ans = []
        for [x, y] in queries:
            if x not in adjList:
                ans.append(-1)
                continue
            visited =  set()
            queue = deque()
            queue.append((x, 1))
            visited.add(x)
            while queue:
                node, val = queue.popleft()
                if node == y:
                    ans.append(val)
                    break
                for (z, mult) in adjList[node]:
                    if z not in visited:
                        visited.add(z)
                        queue.append((z, val*mult))
            if y not in visited:
                ans.append(-1.0)
        return ans

