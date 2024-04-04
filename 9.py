"""
9. Palindrome Number

REALLY BAD LMAO
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = str(x)
        if str(x) == temp[::-1]:
            return True
        return False