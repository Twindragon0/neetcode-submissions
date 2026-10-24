class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1
        numZeros = 0
        for num in nums:
            if num == 0 and numZeros == 0:
                numZeros += 1
            else:
                totalProduct *= num
        output = []
        for num in nums:
            if num == 0 and numZeros == 1:
                output.append(totalProduct)
            elif num == 0 and numZeros > 1:
                output.append(0)
            elif num != 0 and numZeros >= 1:
                output.append(0)
            else:
                output.append(int(totalProduct / num))
        return output


        