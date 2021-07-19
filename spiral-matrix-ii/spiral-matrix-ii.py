class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        def moveR(i,k):
            j = 0
            while j < n:
                if output[i][j] == 0:
                    output[i][j] = k
                    k += 1
                j += 1
            return k
                
        def moveL(i, k):
            j = n-1
            while j >= 0:
                if output[i][j] == 0:
                    output[i][j] = k
                    k += 1
                j -= 1
            return k 
        
        def moveD(j, k):
            i = 0
            while i < n:
                if output[i][j] == 0:
                    output[i][j] = k
                    k += 1
                i += 1
            return k
        
        def moveU(j, k):

            i = n-1
            while i >= 0:
                if output[i][j] == 0:
                    output[i][j] = k
                    k += 1
                i -= 1
            return k
        
        
        
        output = [[0]*n for _ in range(n)]
        k = 1
        for i in range(n):
            k = moveR(i,k)
            k = moveD(n-i-1, k)
            k = moveL(n-i-1, k)
            k = moveU(i, k)
        return output
                
            
            
        