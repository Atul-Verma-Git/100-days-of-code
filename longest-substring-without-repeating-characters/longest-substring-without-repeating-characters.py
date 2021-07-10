class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        m = 0
        s_index = 0
        char_dict = {}
        for _ in range(len(s)):
            if s[_] not in char_dict.keys():
                m += 1
                char_dict[s[_]] = _
            else:
                if s_index <= char_dict[s[_]]:
                    s_index = char_dict[s[_]]+1
                    ans = max(m,ans)
                    m = _ - (s_index-1)
                    char_dict[s[_]] = _
                else:
                    m += 1
                    char_dict[s[_]] = _
        
        return max(m , ans)
            
            
        
        