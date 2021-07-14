class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for _ in range(len(s)):
            if s[_] not in s_dict.keys():
                s_dict[s[_]] = t[_]
            else:
                if s_dict[s[_]] != t[_]:
                    return False
            if t[_] not in t_dict.keys():
                t_dict[t[_]] = s[_]
            else:
                if t_dict[t[_]] != s[_]:
                    return False
        return True