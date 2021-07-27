class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def convert(num):
            numb = 0
            for n in num:
                numb = numb * 10 + int(n)
            return numb
        return str(convert(num1) * convert(num2))
        