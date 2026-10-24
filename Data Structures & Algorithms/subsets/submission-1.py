class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for num in nums:
            n = len(ans)
            for i in range(n):
                newArr = ans[i].copy()
                newArr.append(num)
                ans.append(newArr)
        return ans
