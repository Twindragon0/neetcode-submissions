class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort(reverse=True)
        def recurse(i, kFilled):
            if i == len(nums):
                return all(el == (sum(nums) // k) for el in kFilled)
            else:
                for j in range(k):
                    if kFilled[j] > sum(nums) // k:
                        break
                    kFilled[j] += nums[i]
                    if recurse(i+1, kFilled):
                        return True
                    kFilled[j] -= nums[i]
                    if kFilled[j] == 0:
                        break
                return False
        return recurse(0, [0] * k)