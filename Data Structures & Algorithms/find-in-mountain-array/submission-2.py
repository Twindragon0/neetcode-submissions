class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        pivot = -1
        l = 0
        r = mountainArr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            curr = mountainArr.get(mid)
            prev = mountainArr.get(mid-1)
            nxt = mountainArr.get(mid+1)

            if curr > prev and curr > nxt:
                pivot = mid
                break
            elif prev < curr:
                l = mid + 1
            else:
                r = mid - 1
        
        l = 0
        r = pivot
        while l <= r:
            mid = (l + r) // 2
            curr = mountainArr.get(mid)
            if curr < target:
                l = mid + 1
            elif curr > target:
                r = mid - 1
            else:
                return mid
        l = pivot+1
        r = mountainArr.length() - 1
        while l <= r:
            mid = (l + r) // 2
            curr = mountainArr.get(mid)
            if curr < target:
                r = mid - 1
            elif curr > target:
                l = mid + 1
            else:
                return mid
        return -1
