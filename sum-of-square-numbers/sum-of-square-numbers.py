class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        import math
        for i in range(int(math.sqrt(c)) + 1 ):
            num = c - i * i
            x = math.sqrt(num)
            if x == int(x):
                return True
        return False
        