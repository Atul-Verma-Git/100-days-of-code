class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        output = []
        for i in range(rowIndex+1):
            j = 0
            temp = []
            while j <= i:
                if j == 0 or j == i:
                    temp.append(1)
                    j += 1
                else:
                    temp.append(output[i-1][j] + output[i-1][j-1])
                    j += 1
            output.append(temp)
        return output[rowIndex]
        
        