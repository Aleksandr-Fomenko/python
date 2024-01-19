from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(Counter(text)[k] // v for k, v in Counter("balloon").items())

if __name__ == '__main__':
    print(Solution().maxNumberOfBalloons(text = "nlaebolko"))
    print(Solution().maxNumberOfBalloons(text = "loonbalxballpoon"))
    print(Solution().maxNumberOfBalloons(text = "leetcode"))

