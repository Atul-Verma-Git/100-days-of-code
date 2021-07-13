class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = []
        def rotate(matrix):
            while matrix[0] != []: 
                output.append(matrix[0][0])
                del matrix[0][0]
            for i in range(1,len(matrix)):
                if matrix[i] != []:
                    output.append(matrix[i][len(matrix[i])-1])
                    del matrix[i][len(matrix[i])-1]
            while matrix[len(matrix)-1]:
                output.append(matrix[len(matrix)-1][len(matrix[i])-1])
                del matrix[len(matrix)-1][len(matrix[i])-1]
            for i in reversed(range(1,len(matrix)-1)):
                if matrix[i] != []:
                    output.append(matrix[i][0])
                    del matrix[i][0]
            matrix = [_ for _ in matrix if _ != []]
            if matrix != []:
                rotate(matrix)
        rotate(matrix)
        return output
                                        
                                
                            
        