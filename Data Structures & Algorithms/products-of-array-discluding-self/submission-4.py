class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftPrefixSum = [0] * len(nums)
        rightPrefixSum = [0] * len(nums)
        leftPrefixSum[0] = nums[0]
        rightPrefixSum[len(nums)-1] = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            leftPrefixSum[i] = leftPrefixSum[i-1] * nums[i]
        for i in range(len(nums)-2, -1, -1):
            rightPrefixSum[i] = rightPrefixSum[i+1] * nums[i]
        output = []
        for i in range(len(nums)):
            ans = 1
            if i-1 >= 0:
                ans *= leftPrefixSum[i-1]
            if i+1 < len(nums):
                ans *= rightPrefixSum[i+1]
            output.append(ans)
        return output


        