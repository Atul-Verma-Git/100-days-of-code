class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        d = {n:0}
        while n != 1:
            output = 0 
            while n != 0:
                n , num = divmod(n, 10)
                output += num * num
            if output == 1:
                return True
            if output not in d.keys():
                d[output] = 0
                n = output
            else:
                return False
        return True
                
        