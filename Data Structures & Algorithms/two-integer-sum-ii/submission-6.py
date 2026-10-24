class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mappings = defaultdict(int)
        for i, num in enumerate(numbers):
            if target-num in mappings:
                return [mappings[target-num]+1, i+1]
            mappings[num] = i
        return [-1,-1]
