class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.ans = set()
        nums.sort()
        def recurse(i, subset):
            if i == len(nums):
                self.ans.add(tuple(subset))
            else:
                self.ans.add(tuple(subset))
                subset.append(nums[i])
                recurse(i+1, subset)
                subset.pop(-1)
                recurse(i+1, subset)

        recurse(0, [])
        return [list(el) for el in self.ans]