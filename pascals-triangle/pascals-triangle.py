class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = []
        for i in range(numRows):
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
        return output
        