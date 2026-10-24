class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for mask in range(1 << n):
            curr = 0
            for i in range(n):
                if mask & (1 << i):
                    curr ^= nums[i]
            ans += curr
        return ans
