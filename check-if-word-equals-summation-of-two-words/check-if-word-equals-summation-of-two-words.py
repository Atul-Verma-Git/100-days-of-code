class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        first=0
        for _ in range(len(firstWord)):
            first = 10*first+(ord(firstWord[_])-ord('a'))

        second=0
        for _ in range(len(secondWord)):
            second = 10*second+(ord(secondWord[_])-ord('a'))    

        target=0
        for _ in range(len(targetWord)):
            target = 10*target+(ord(targetWord[_])-ord('a')) 

        print(first,second,target)
        if first+second == target:
            return True
        else:
            return False