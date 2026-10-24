import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        negatives = []
        positives = []
        for num in nums:
            if num < 0:
                negatives.append(-1 * num)
            else:
                positives.append(num)
        d = 1
        while len(negatives) >= 1 and max(negatives) // d != 0:
            negatives = self.radixSort(negatives, d)
            d *= 10
        d = 1
        while len(positives) >= 1 and max(positives) // d != 0:
            positives = self.radixSort(positives, d)
            d *= 10
        return list(reversed([-1 * num for num in negatives])) + positives

    def radixSort(self, nums: List[int], d: int) -> List[int]:
        count = [0] * 10
        for num in nums:
            count[(num // d) % 10] += 1
        for i in range(1,10):
            count[i] += count[i-1]
        res = [0] * len(nums)
        for i in range(len(nums)-1,-1,-1):
            res[count[(nums[i] // d) % 10] - 1] = nums[i]
            count[(nums[i] // d) % 10] -= 1
        return res
        


