import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # better algorithm O(log n)
        l, r = 0, len(nums) - 1
        while l <= r:
            # overflow protection by doing this just incase we have a question about overflow issues this solves it
            m = l + ((r - l) // 2)
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

        # brute force O(n)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1