class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        left = 0
        right = 0
        while left < m or right < n:
            if left == m:
                tmp.append(nums2[right])
                right += 1
            elif right == n:
                tmp.append(nums1[left])
                left += 1
            elif nums1[left] <= nums2[right]:
                tmp.append(nums1[left])
                left += 1
            else:
                tmp.append(nums2[right])
                right += 1
        for i in range(len(tmp)):
            nums1[i] = tmp[i]