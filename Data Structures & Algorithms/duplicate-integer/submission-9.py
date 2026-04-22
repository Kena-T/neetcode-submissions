class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 1. The problem is asking: Find duplicates in the list and return True if there is any duplicates False if not
        # 2. Brute force is: a double for loop which is O(n^2) because it requires you to look at every element and check if its in the list twice
        # 3. To speed it up, I need to: track what I have already seen and use that to check that the next element is something I have't seen (look up / track / skip / sort / etc.)
        # 4. So I use a ___ where the key is ___ and the value is ___
        
        # better algorithm
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False


        #brute force O(n^2)
        for i in range(len(nums)):
            for j in nums[i+1:]:
                if nums[i] == j:
                    return True
        
        return False