class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_dict = {}
        for i in s:
            if i not in my_dict.keys():
                my_dict[i] = 1
            else:
                my_dict[i] += 1
        for i in t:
            if i not in my_dict.keys():
                return False
            else:
                my_dict[i] -= 1
                if my_dict[i] == 0:
                    del my_dict[i]
        sum = 0        
        for _ in my_dict.keys():
            sum += my_dict[_]
        if sum == 0:
            return True
        return False
        