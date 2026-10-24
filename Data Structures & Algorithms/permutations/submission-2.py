class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def recurse(mask, subset):
            if len(subset) == len(nums):
                self.ans.append(subset.copy())
            for i in range(len(nums)):
                if not mask & (1 << i):
                    subset.append(nums[i])
                    recurse(mask | (1 << i), subset)
                    subset.pop(-1)
        recurse(0, [])
        return self.ans
