class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return True if sorted(s) == sorted(t) else False

if __name__ == '__main__':
    print(Solution().isAnagram(s = "anagram", t = "nagaram"))
    print(Solution().isAnagram(s = "rat", t = "car"))
