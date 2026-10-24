class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = []
        total = (len(nums1) + len(nums2)) // 2 + 1
        p1 = 0
        p2 = 0
        added = 0
        while added < total:
            if p1 == len(nums1):
                combined.append(nums2[p2])
                p2 += 1
            elif p2 == len(nums2):
                combined.append(nums1[p1])
                p1 += 1
            elif nums1[p1] <= nums2[p2]:
                combined.append(nums1[p1])
                p1 += 1
            else:
                combined.append(nums2[p2])
                p2 += 1
            added += 1
        if (len(nums1) + len(nums2)) % 2 == 0:
            return (combined[-1] + combined[-2]) / 2
        else:
            return combined[-1]
