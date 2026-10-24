class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0
        def recurse(i, subset):
            curr = 0
            for num in subset:
                curr ^= num
            self.ans += curr
            for j in range(i, len(nums)):
                subset.append(nums[j])
                recurse(j+1, subset)
                subset.pop(-1)
        recurse(0, [])
        return self.ans