import re

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        infoList = [ i.start() for i in re.finditer(needle, haystack)]
        if len(infoList) == 0:
            return -1
        else:
            return infoList[0]


if __name__ == '__main__':
    print(Solution().strStr(haystack = "sadbutsad", needle = "sad"))
    print(Solution().strStr(haystack = "leetcode", needle = "leeto"))
