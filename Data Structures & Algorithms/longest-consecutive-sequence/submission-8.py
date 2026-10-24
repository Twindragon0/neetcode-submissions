class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numToLength = defaultdict(int)
        ans = 0
        for num in nums:
            if not numToLength[num]:
                numToLength[num] = 1 + numToLength[num+1] + numToLength[num-1]
                numToLength[num - numToLength[num-1]] = numToLength[num]
                numToLength[num + numToLength[num+1]] = numToLength[num]
                ans = max(ans, numToLength[num])
        return ans
            


            

