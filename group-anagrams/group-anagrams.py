class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        l = {}
        for i in range(len(strs)):
            d = {}
            for j in range(len(strs[i])):
                if strs[i][j] in d.keys():
                    d[strs[i][j]] += 1
                else:
                    d[strs[i][j]] = 1
            l[strs[i]] = d
        
        output = []
        while strs != []:
            curr = [strs[0]]
            i = 1
            while i < len(strs):
                if l[strs[0]] == l[strs[i]]:
                    curr.append(strs[i])
                    del strs[i]
                else:
                    i += 1
            del strs[0]
            output.append(curr)
        return output
            
        '''
        d = {}
        for s in sorted(strs):
            key = tuple(sorted(s))
            d[key] = d.get(key, []) + [s]
        return d.values()
