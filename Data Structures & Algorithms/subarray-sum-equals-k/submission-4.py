class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = [0] * (len(nums) + 1)
        frequencies = defaultdict(int)
        ans = 0
        for i in range(1, len(nums)+1):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]
            if prefixSum[i] == k:
                ans += 1
            ans += frequencies[prefixSum[i] - k]
            frequencies[prefixSum[i]] += 1
        return ans
                
