class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums)-k
        def quickSelect(l, r):
            pivot = nums[r]
            smallerThan = l-1
            for i in range(l, r):
                if nums[i] <= pivot:
                    smallerThan += 1
                    nums[i], nums[smallerThan] = nums[smallerThan], nums[i]
            smallerThan += 1
            nums[r], nums[smallerThan] = nums[smallerThan], nums[r]
            if smallerThan == k:
                return nums[smallerThan]
            elif smallerThan < k:
                return quickSelect(smallerThan+1, r)
            else:
                return quickSelect(l, smallerThan-1)
        return quickSelect(0, len(nums)-1)
