class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        def mult(start, end):
            if start == end:
                return start
            else:
                return end * mult(start,end-1)
        return mult(n+2 , 2*n) // mult(2,n)
        