class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # APPROACH 1
        ans = []
        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)
        return ans