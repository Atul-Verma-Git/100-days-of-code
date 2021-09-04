class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        i = 0
        temp = []
        word_count = 0
        no_word = 0
        while i < len(words):
            word_count += (len(words[i])+1)
            if word_count-1 <= maxWidth:
                temp.append(words[i])
                no_word += 1
                i += 1
            else:
                space = maxWidth - (word_count - len(words[i]))+2
                if no_word > 1:
                    x, y = divmod(space, no_word-1)
                    s = ''
                    t = 0
                    while y:
                        s += (temp[t]+ ' ' + ' '*(x+1))
                        y -= 1
                        t += 1
                    while t < len(temp):
                        if t == len(temp)-1:
                            s += (temp[t])
                            t += 1
                        else:
                            s += (temp[t]+ ' ' + ' '*(x))
                            t += 1
                    output.append(s)
                else:
                    s = '' + temp[0] + ' '*(maxWidth- len(temp[0]))
                    output.append(s)
                temp = []
                word_count = 0
                no_word = 0
        temp = " ".join(temp)
        temp += ' '*(maxWidth- len(temp))
        
        output.append(temp)
        return output
            
        
        