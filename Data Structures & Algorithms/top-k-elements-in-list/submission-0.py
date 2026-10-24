class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyMap = defaultdict(int)
        for num in nums:
            frequencyMap[num] += 1
        tup = sorted(frequencyMap.items(), key=lambda x: x[1], reverse=True)[:k]
        return [el[0] for el in tup]
        