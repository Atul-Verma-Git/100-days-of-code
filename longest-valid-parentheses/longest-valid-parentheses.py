class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if s == "":
            return 0
        stack = [-1]
        maxh = 0
        height = 0
        for i, p in enumerate(s):
            if p == '(':
                stack.append(i)
            if p == ')':
                stack.pop()
                if stack == []:
                    stack.append(i)
                else:
                    height = i - stack[-1]
                    maxh = max(maxh, height)
        return maxh
                