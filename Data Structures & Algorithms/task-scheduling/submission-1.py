class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskToFreq = defaultdict(int)
        for task in tasks:
            taskToFreq[task] += 1
        arr = [(freq, task) for task, freq in taskToFreq.items()]
        arr.sort(reverse=True)
        maxVal = arr[0][0]
        numIdle = (maxVal-1)*n
        for i in range(1, len(arr)):
            numIdle -= min(maxVal-1, arr[i][0])
        return max(0, numIdle) + len(tasks)
        