class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if not len(A) <= len(B):
            B, A = nums1, nums2

        l = -1
        r = len(A) - 1
        numEls = (len(A) + len(B) + 1) // 2
        while l <= r:
            i = (l + r) // 2
            # (i - 0 + 1) + (j - 0 + 1) = numEls
            j = numEls - i - 2

            Aleft = A[i] if i >= 0 else -1
            Aright = A[i+1] if i+1 < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else -1
            Bright = B[j+1] if j+1 < len(B) else float("inf")

            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                return max(Aleft, Bleft)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
