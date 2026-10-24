class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            val = target - numbers[i]
            left = i+1
            right = len(numbers) - 1
            while left <= right:
                mid = (left+right) // 2
                if numbers[mid] == val:
                    return [i+1, mid+1]
                if numbers[mid] > val:
                    right = mid-1
                else:
                    left = mid+1
        return [-1,-1]