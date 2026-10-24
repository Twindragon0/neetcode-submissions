class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
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
