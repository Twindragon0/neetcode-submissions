class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        buckets = [[] for _ in range(len(nums))]
        for (num, freq) in frequency.items():
            buckets[freq-1].append(num)
        ans = []
        for i in range(len(nums) - 1, -1, -1):
            if len(ans) != k:
                ans.extend(buckets[i])
        return ans
