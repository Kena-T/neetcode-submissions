class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. The problem is asking: is the string a valid palindrome reading the same forward and backwards
        # 2. Brute force: I used a single for loop which is O(n) because it needs to loop through n characters and make sure they are a numer or a alphabet charater and nothing else.
        # 3. To speed it up, I need to: Find a way to check that the front and the back of the string at the same time and shift at the same time to check if its a palindrome
        # 4. So I use two pointer to check left and right at the same time — two pointers would help us check both sides of the string at the same time.

        # better solution O()
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            r -= 1
            l += 1
        return True
            

        # Brute force O(n)
        cleaned  = ""
        for c in s:
            if c.isalnum():
                cleaned += c.lower()
        
        reversed_cleaned = cleaned[::-1]
        return cleaned == reversed_cleaned
    
    def alphaNum(self, c: str) -> bool:
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))