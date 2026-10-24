class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        inDegree = [0] * numCourses
        courseMap = defaultdict(list)
        for (a, b) in prerequisites:
            inDegree[a] += 1
            courseMap[b].append(a)
        
        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)
        ans = []
        while queue:
            course = queue.popleft()
            ans.append(course)
            for unlocked in courseMap[course]:
                inDegree[unlocked] -= 1
                if inDegree[unlocked] == 0:
                    queue.append(unlocked)
        if len(ans) == numCourses:
            return ans
        return []
