class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans = []
        def recurse(i, curr):
            self.ans.append(list(curr))
            for j in range(i, len(nums)):
                curr.append(nums[j])
                recurse(j+1, curr)
                curr.pop(-1)
        recurse(0, [])
        return self.ans