class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, -1, -1):
            j = i + 1
            while j < len(temperatures) and temperatures[j] <= temperatures[i]:
                if ans[j] == 0:
                    j = len(temperatures)
                    break
                else:
                    j += ans[j]
            if j < len(temperatures):
                ans[i] = j - i
        return ans
