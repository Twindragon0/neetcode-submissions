class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = nums[(0-k) % len(nums)]
        curr = 0
        counter = 0
        while counter != len(nums):
            val = nums[curr]
            nums[curr] = tmp
            tmp = val
            counter += 1
            curr = (curr + k) % len(nums)
            if (counter % (len(nums)/math.gcd(len(nums),k)) == 0):
                curr += 1
                tmp = nums[(curr-k) % len(nums)]