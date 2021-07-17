class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        s = re.findall('(^[\+\-0]*\d+)\D*', s)
        print(s)
        try :
            s = int(s[0])

            if s >= -1<<31 and s < 1<<31:
                return s
            else:
                if s < 0:
                    return -1<<31
                else:
                    return (1<<31)-1
        except:
            return 0
        
            
        