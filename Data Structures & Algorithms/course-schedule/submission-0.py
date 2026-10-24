class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        inDegree = [0] * numCourses
        courseMap = defaultdict(list)
        for (a, b) in prerequisites:
            inDegree[a] += 1
            courseMap[b].append(a)

        queue = deque()
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                queue.append(i)
        while queue:
            course = queue.popleft()
            for unlocked in courseMap[course]:
                inDegree[unlocked] -= 1
                if inDegree[unlocked] == 0:
                    queue.append(unlocked)
        return sum(inDegree) == 0
