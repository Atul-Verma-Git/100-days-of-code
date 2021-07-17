class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        output = []
        d = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],\
            6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
        if digits == '':
            return output
        output = d[int(digits[0])]
        for i in digits[1:]:
            temp = []
            for j in range(len(output)):
                for k in range(len(d[int(i)])):
                    temp.append(output[j] + d[int(i)][k])
            output = temp
        return output
            
        