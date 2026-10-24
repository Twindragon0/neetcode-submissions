class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskToFreq = defaultdict(int)
        for task in tasks:
            taskToFreq[task] += 1
        arr = [freq for task, freq in taskToFreq.items()]
        maxVal = max(taskToFreq.values())
        maxItems = 0
        for freq in arr:
            if freq == maxVal:
                maxItems += 1
        return max((maxVal-1) * (n+1) + maxItems, len(tasks))
        