class Solution:
    def maxValue(self, n: str, x: int) -> str:
        ans=[]
        if n[0] == '-':
            ans.append(n[0])
            for _ in range(1,len(n)):
                if int(n[_]) <= x:
                    ans.append(n[_])
                else:
                    ans.append(str(x))
                    ans.append(n[_:])
                    break 
            if len(''.join(ans)) == len(n):
                ans.append(str(x))


        else:
            for _ in range(len(n)):
                if int(n[_]) >= x:
                    ans.append(n[_])
                else:
                    ans.append(str(x))
                    ans.append(n[_:])
                    break

            if len(''.join(ans)) == len(n):
                ans.append(str(x))
        return ''.join(ans)

