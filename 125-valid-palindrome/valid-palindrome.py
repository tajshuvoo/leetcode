class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) > (2 * 10**5):
            return False

        old = ""

        for i in range(len(s)):
            if s[i].isalnum():
                old += s[i]

        old=old.lower()
        new= old[::-1]
        return new==old