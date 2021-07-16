class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p = s1
        s = s2
        p_dict = {}
        for i in range(len(p)):
            if p[i] not in p_dict.keys():
                p_dict[p[i]] = 1
            else:
                p_dict[p[i]] += 1
        i = 0    
        s_dict = {}
        start = 0
        while i < len(p) and i < len(s):
            if s[i] not in s_dict.keys():
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
            i += 1
        output = []
        end = len(p)
        while end < len(s):
            if s_dict == p_dict:
                return True
            s_dict[s[start]] -= 1
            if s_dict[s[start]] == 0:
                del s_dict[s[start]]
            if s[end] not in s_dict.keys():
                 s_dict[s[end]] = 1
            else:
                 s_dict[s[end]] += 1
            start += 1
            end += 1
        if s_dict == p_dict:
            return True            
        return False
        