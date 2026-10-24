class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
        frequency = sorted(frequency.items(), key=lambda x: -x[1])
        ans = [num for (num, val) in frequency[:k]]
        return ans