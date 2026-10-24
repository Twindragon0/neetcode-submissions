class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.totalSum = sum(nums)
        self.memo = defaultdict(int)
        def recurse(i, curr):
            if (i, curr) in self.memo:
                return self.memo[(i, curr)]
            if i >= len(nums) and curr - (self.totalSum - curr) == target:
                return 1
            if i >= len(nums):
                return 0
            self.memo[(i, curr)] = recurse(i+1, curr) + recurse(i+1, curr+nums[i])
            return self.memo[(i, curr)]
        return recurse(0, 0)