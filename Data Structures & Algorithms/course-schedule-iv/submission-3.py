class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adjList = defaultdict(list)
        for (x, y) in prerequisites:
            adjList[x].append(y)
        ans = []
        prerequisiteList = defaultdict(set)
        for i in range(numCourses):
            queue = deque()
            queue.append(i)
            while queue:
                x = queue.popleft()
                if x < i:
                    prerequisiteList[i].update(prerequisiteList[x])
                else:
                    for y in adjList[x]:
                        prerequisiteList[i].add(y)
                        queue.append(y)
        ans = []
        for [first, second] in queries:
            ans.append(second in prerequisiteList[first])
        return ans
        