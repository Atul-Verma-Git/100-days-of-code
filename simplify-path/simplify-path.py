class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split("/")
        path = [_ for _ in path if _ != ""]
        stack = []
        for i in path:
            if i == '.':
                pass
            elif i == '..':
                if stack != []:
                    stack.pop()
            else:
                stack.append(i)
        output = ''
        for i in stack:
            output += '/'+i
        if output == '':
            return '/'
        return output
        