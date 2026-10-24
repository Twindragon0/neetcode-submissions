class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = [0] * len(nums)
        rightProd = [0] * len(nums)

        leftProd[0] = nums[0]
        for i in range(1, len(nums)):
            leftProd[i] = nums[i] * leftProd[i-1]

        rightProd[len(nums) - 1] = nums[len(nums)- 1]
        for i in range(len(nums)-2,-1,-1):
            rightProd[i] = nums[i] * rightProd[i+1]
        
        ans = [1] * len(nums)
        for i in range(len(nums)):
            if i != 0:
                ans[i] *= leftProd[i-1]
            if i != len(nums) - 1:
                ans[i] *= rightProd[i+1]
        return ans

        