class Solution:
    def isPalindrome(self, x: int) -> bool:
        b = str(x)
        a = list(reversed(b))
        a = (str(''.join(a)))
        if a == b:
            return True
        else:
            return False