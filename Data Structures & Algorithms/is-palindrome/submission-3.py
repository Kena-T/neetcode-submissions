class Solution:
    def isPalindrome(self, s: str) -> bool:
        #brute force O()
        clean = re.sub(r'[^a-zA-Z0-9]', '', s)
        return clean.lower() == clean[::-1].lower()