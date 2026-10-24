class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        def recurse(i, curr, lst):
            if curr > target or i >= len(nums):
                return
            elif curr == target:
                self.ans.append(lst.copy())
            else:
                lst.append(nums[i])
                recurse(i, curr+nums[i], lst)
                lst.pop(-1)
                recurse(i+1, curr, lst)
        recurse(0, 0, [])
        return self.ans