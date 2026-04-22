class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 1. The problem is asking: Find and remove duplicates while adding up the number of uniqe elements into variable k
        # 2. Brute force is: double while loop which is O(n^2) because it has to check n elements twice to check for duplicates
        # 3. To speed it up, I need to: create a way to check the list of numbers for its neighbor and skip if it's not equal reducing the O(n) or less.
        # 4. So I use [tool] to [action] — [brief mechanism]

        # Better Algorithm O()
        l, r = 0, 1
        while r < len(nums):
            if nums[l] == nums[r]:
                r += 1
                continue
            l += 1
            nums[l] = nums[r]
        
        return l + 1
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