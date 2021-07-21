class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        out = [[0]*(i+1) for i in range(len(triangle))]
        out[0][0] = triangle[0][0]
        for i in range(1,len(triangle)):
            for j in range(1,len(triangle[i-1])):
                out[i][j] = min(out[i-1][j]+triangle[i][j], out[i-1][j-1]+triangle[i][j])
            out[i][0] = out[i-1][0] + triangle[i][0] 
            out[i][i] = out[i-1][i-1] + triangle[i][i] 
        return (min(out[-1]))
        