class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        toWrite = m + n - 1
        while m > 0 and n > 0:
            if nums1[m-1] >= nums2[n-1]:
                nums1[toWrite] = nums1[m-1]
                m -= 1
                toWrite -= 1
            else:
                nums1[toWrite] = nums2[n-1]
                n -= 1
                toWrite -= 1
        while n > 0:
            nums1[toWrite] = nums2[n-1]
            n -= 1
            toWrite -= 1
