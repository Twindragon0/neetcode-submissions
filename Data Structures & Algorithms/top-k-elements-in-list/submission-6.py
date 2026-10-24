class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        bucket = [[] for _ in range(len(nums))]
        for num, freq in frequencies.items():
            bucket[freq - 1].append(num)
        ans = []
        for i in range(len(bucket) - 1, -1, -1):
            if len(ans) != k:
                ans.extend(bucket[i])
        return ans
