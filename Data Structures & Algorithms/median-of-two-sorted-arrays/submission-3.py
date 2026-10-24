class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if not len(A) <= len(B):
            A = nums2
            B = nums1

        l = -1
        r = len(A) - 1
        half = (len(A) + len(B) + 1) // 2
        while l <= r:
            i = (l + r) // 2
            # (i - 0 + 1) + (j - 0 + 1) == half 
            j = half - i - 2
            
            Aright = A[i+1] if i+1 < len(A) else float("inf")
            Bright = B[j+1] if j+1 < len(B) else float("inf")
            Aleft = A[i] if i >= 0 else -1
            Bleft = B[j] if j >= 0 else -1
            print(i)
            print(j)
            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return max(Aleft, Bleft)
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1