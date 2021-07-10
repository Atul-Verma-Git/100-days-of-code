class Solution:
    def reverse(self, x: int) -> int:
        b = str(x)
        if b[0] == '-':
            a = list(reversed(b[1:]))
            a = (int('-'+''.join(a)))
            if a < -2**31:
                return 0
            return a
        else:
            a = list(reversed(b))
            a = (int(''.join(a)))
            if a >= 2**31 :
                return 0
            return a
            
        