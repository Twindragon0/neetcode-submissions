class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 1 # product of everything assuming at most one zero
        numZeros = 0
        for num in nums:
            if num == 0 and numZeros < 1:
                numZeros += 1
            else:
                totalProduct *= num
        output = []
        for num in nums:
            if numZeros >= 1 and num == 0:
                output.append(totalProduct)
            elif numZeros >= 1 and num != 0:
                output.append(0)
            else:
                output.append(int(totalProduct / num))
        return output

        