class Solution:
    def isValid(self, s: str) -> bool:
        while len(s) > 0:
            l = len(s)
            s = s.replace('()','').replace('{}','').replace('[]','')
            if l==len(s): return False
        return True

if __name__ == '__main__':
    print(Solution().isValid(s = "()"))
    print(Solution().isValid(s = "()[]{}"))
    print(Solution().isValid(s = "(]"))
    print(Solution().isValid(s = "([)]"))
    print(Solution().isValid(s="(){}}{"))
    print(Solution().isValid(s="{[]}"))
