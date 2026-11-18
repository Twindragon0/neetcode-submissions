class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def recurse(i, curr):
            for j in range(i, len(nums)):
                recurse(j+1, curr ^ nums[j])
            self.ans += curr
        recurse(0, 0)
        return self.ans

        

