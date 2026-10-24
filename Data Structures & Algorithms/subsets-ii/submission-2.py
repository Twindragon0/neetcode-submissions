class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def recurse(i, subset):
            if i == len(nums):
                self.ans.append(subset.copy())
            else:
                subset.append(nums[i])
                recurse(i+1, subset)
                subset.pop(-1)
                while i+1 < len(nums) and nums[i] == nums[i+1]:
                    i += 1
                recurse(i+1, subset)
        nums.sort()
        recurse(0, [])
        return self.ans