class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        frequencies = defaultdict(int)
        prefixSum = 0
        ans = 0
        for num in nums:
            prefixSum += num
            if prefixSum == k:
                ans += 1
            ans += frequencies[prefixSum-k]
            frequencies[prefixSum] += 1
        return ans

        