class Solution:
    def isThree(self, n: int) -> bool:
        count = 0
        for i in range(1,int(sqrt(n))+1):
            if n % i == 0:
                count += 1
        if (sqrt(n) == int(sqrt(n)) and count*2 -1 == 3):
            return True
        return False
        