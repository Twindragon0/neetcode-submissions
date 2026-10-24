import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums) - 1)
        return nums
    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        mid = int(len(nums) / 2)
        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid:])
        ans = []
        i, j = 0, 0
        while i < len(left) or j < len(right):
            if i == len(left):
                ans.append(right[j])
                j += 1
            elif j == len(right):
                ans.append(left[i])
                i += 1
            elif left[i] <= right[j]:
                ans.append(left[i])
                i += 1
            else:
                ans.append(right[j])
                j += 1
        return ans

    def quickSort(self, nums: List[int], lo: int, hi: int):
        if lo >= hi:
            return
        pivot_index = random.randint(lo, hi)
        nums[pivot_index], nums[hi] = nums[hi], nums[pivot_index]

        swapIndex = lo-1
        for i in range(lo, hi):
            if nums[i] < nums[hi]:
                swapIndex += 1
                nums[i], nums[swapIndex] = nums[swapIndex], nums[i]
        swapIndex += 1
        nums[hi], nums[swapIndex] = nums[swapIndex], nums[hi]
        self.quickSort(nums, lo, swapIndex - 1)
        self.quickSort(nums, swapIndex + 1, hi)
        


