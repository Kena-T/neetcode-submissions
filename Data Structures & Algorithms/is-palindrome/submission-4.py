class Solution:
    def isPalindrome(self, s: str) -> bool:
        #better algorithm O()
        arr = []
        for c in s:
            if c.isalnum():
                arr.append(c.lower())
        st = ''.join(arr)
        l, r = 0, len(st)-1
        while l < r:
            if st[l] != st[r]:
                return False
            l += 1
            r -= 1
        return True

        #brute force O(n)
        clean = re.sub(r'[^a-zA-Z0-9]', '', s)
        return clean.lower() == clean[::-1].lower()