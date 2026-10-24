class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        frequencies = defaultdict(int)
        prefix = [0] * len(nums)
        ans = 0
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = prefix[i-1] + nums[i]
            if prefix[i] == k:
                ans += 1
            ans += frequencies[prefix[i] - k]
            frequencies[prefix[i]] += 1
        return ans
        