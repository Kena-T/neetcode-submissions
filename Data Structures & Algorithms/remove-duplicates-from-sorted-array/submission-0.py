class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1. The problem is asking: Find and remove duplicates while adding up the number of uniqe elements into variable k
        # 2. Brute force is: ___ which is O(___) because ___
        # 3. To speed it up, I need to: ___
        # 4. So I use [tool] to [action] — [brief mechanism]

        # Brute force O(n^2)
        k = 0
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    nums.pop(j)
                else:
                    j += 1
            i += 1
        return len(nums)
        
        return k