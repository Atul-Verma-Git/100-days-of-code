'''
s = "leetcode", wordDict = ["leet","code"]
dictionary -> {l:{4:['leet']},c:{4:['code']}}
if "" : True
else

'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in wordDict for j in range(i)),
        return ok[-1]
                                        
            
            
            
            