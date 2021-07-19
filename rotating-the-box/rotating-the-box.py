class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in range(len(box)):
            count = 0
            for j in reversed(range(len(box[0]))):
                if box[i][j] == '.':
                    count += 1
                if box[i][j] == '*':
                    count = 0
                if box[i][j] == '#':
                    box[i][j] = '.'
                    box[i][j+count] = '#'
        output = []
        for j in range(len(box[0])):
            temp = []
            for i in reversed(range(len(box))):
                temp.append(box[i][j])
            output.append(temp)
        return output
                
            

        