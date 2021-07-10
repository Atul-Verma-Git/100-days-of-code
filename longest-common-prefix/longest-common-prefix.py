class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lp = strs[0]
        for _ in range(1,len(strs)):
            count = 0
            for __ in range(min(len(strs[_]),len(lp))):
                if strs[_][__] == lp[__]:
                    count += 1
                else:
                    break
            lp = lp[0:count]
        return lp
        