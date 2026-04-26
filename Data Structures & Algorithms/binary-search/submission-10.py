import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Better algortithm O(log n)
        l, r = 0, len(nums) - 1
        while l <= r:
            # This is just incase we have to deal with overflow 
            m = l + ((r - l) // 2)
            # m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

        # Brute Force O(n) needs to be O(log n) so not good enough
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1