class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1 + nums2
        combined.sort()
        if len(combined) % 2 == 0:
            return (combined[len(combined) // 2] + combined[len(combined) // 2 - 1]) / 2
        return combined[len(combined) // 2]
