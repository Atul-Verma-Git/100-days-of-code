class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        def simplify(s):
            dis1 = 0
            dis2 = 0
            rotate = 0
            for i in range(len(s)):
                if s[i] == 'G':
                    if rotate == 0:
                        dis1 += 1
                    if rotate == 2:
                        dis1 -= 1
                    if rotate == 1:
                        dis2 += 1
                    if rotate == 3:
                        dis2 -= 1
                if s[i] == 'L':
                    if rotate == 0:
                        rotate = 3
                    else:
                        rotate -= 1
                if s[i] == 'R':
                    if rotate == 3:
                        rotate = 0
                    else:
                        rotate += 1
            
            return rotate, dis1, dis2
        b, a, c = simplify(instructions)
        if a == 0 and c == 0:
            return True
        if b != 0:
            return True
        return False
                        
                    
        