class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = set()
        frequencies = defaultdict(int)
        for num in nums:
            frequencies[num] += 1
            if frequencies[num] > (len(nums) // 3):
                ans.add(num)
        return list(ans)
        