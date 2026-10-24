class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        pivot = -1
        l = 0
        r = mountainArr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            curr = mountainArr.get(mid)
            nxt = mountainArr.get(mid+1)
            prev = mountainArr.get(mid-1)
            if curr > prev and curr > nxt:
                pivot = mid
                break
            elif prev < curr < nxt:
                l = mid + 1
            else:
                r = mid - 1
        
        l = 0
        r = pivot
        while l <= r:
            mid = (l + r) // 2
            curr = mountainArr.get(mid)
            if curr == target:
                return mid
            elif curr < target:
                l = mid + 1
            else:
                r = mid - 1
        l = pivot
        r = mountainArr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            curr = mountainArr.get(mid)
            if curr == target:
                return mid
            elif curr < target:
                r = mid - 1
            else:
                l = mid + 1
        return -1