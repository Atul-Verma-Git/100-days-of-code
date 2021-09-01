class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        output = []
        t = len(s)
        w = len(words)
        l = len(words[0])
        d = {}
        for i in words:
            d.setdefault(i,0)
            d[i] += 1
        
        
        for i in range(l):
            match = 0
            copyd = d.copy()
            while i < t:
                copyd.setdefault(s[i:i+l], -1)
                if copyd[s[i:i+l]] == -1:
                    match = 0
                    copyd = d.copy()
                    i = i+l
                else:
                    if copyd[s[i:i+l]] > 0:
                        copyd[s[i:i+l]] -= 1
                        match += 1
                        i += l
                        if match == w:
                            output.append(i-(l*w))
                    else:
                        j = max(0, i - (match*l))
                        while True:                        
                            if s[j:j+l] == s[i:i+l]:
                                copyd[s[j:j+l]] += 1
                                match -= 1
                                break
                            else:
                                copyd[s[j:j+l]] += 1
                                match -= 1
                                j += l
                        copyd[s[i:i+l]] -= 1
                        match += 1
                        i += l
                        if match == w:
                            output.append(i-(l*w))

        return output
    
        
        