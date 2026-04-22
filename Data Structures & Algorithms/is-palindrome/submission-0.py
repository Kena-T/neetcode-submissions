class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. The problem is asking: is the string a valid palindrome reading the same forward and backwards
        # 2. Brute force: ___ which is O(___) because ___
        # 3. To speed it up, I need to: ___
        # 4. So I use [tool] to [action] — [brief mechanism]


        # Brute force O()
        cleaned  = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        
        reversed_cleaned = cleaned[::-1]
        return cleaned == reversed_cleaned