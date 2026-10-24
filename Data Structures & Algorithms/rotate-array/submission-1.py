import math
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numVisited = 0
        curr = 0
        tmp = nums[(curr-k) % len(nums)]
        while numVisited < len(nums):
            val = nums[curr]
            nums[curr] = tmp
            tmp = val

            numVisited += 1
            curr = (curr + k) % len(nums)
            if numVisited % (len(nums) // (math.gcd(len(nums), k))) == 0:
                curr += 1
                tmp = nums[(curr-k) % len(nums)]

            
