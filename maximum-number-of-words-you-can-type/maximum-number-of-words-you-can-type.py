class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        b = list(brokenLetters)
        text = text.split()
        i = 0
        while i < (len(text)):
            flag = 0
            for j in range(len(text[i])):
                if text[i][j] in b:
                    del text[i]
                    flag = 1
                    break
            if flag == 0:
                i += 1
            
        return len(text)
        