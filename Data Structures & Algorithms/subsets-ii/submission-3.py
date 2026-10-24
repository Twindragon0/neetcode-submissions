class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def recurse(i, subset):
            self.ans.append(subset.copy())
            for j in range(i, len(nums)):
                if j > i and nums[j] == nums[j-1]:
                    continue
                subset.append(nums[j])
                recurse(j+1, subset)
                subset.pop(-1)
        nums.sort()
        recurse(0, [])
        return self.ans