class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
        frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
        ans = [num for (num, freq) in frequencies[:k]]
        return ans
