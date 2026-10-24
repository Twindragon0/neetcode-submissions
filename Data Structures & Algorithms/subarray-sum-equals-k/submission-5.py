class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # [2, -1, 1, 2]
        # [2, 1, 2, 4]
        # for i element that we're on
        # 1. if that is k, then we add one to the result
        # 2. if prefixsum[i]-k has been looked at, then we add number of times it appears to result
        ans = 0
        prefixSum = [0] * (len(nums)+1)
        frequency = defaultdict(int)
        for i in range(1, len(prefixSum)):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]
            if prefixSum[i] == k:
                ans += 1
            ans += frequency[prefixSum[i] - k]
            frequency[prefixSum[i]] += 1
        return ans
                
