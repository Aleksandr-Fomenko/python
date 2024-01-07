import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return int(math.sqrt(x))


if __name__ == '__main__':
    print(Solution().mySqrt(4))
    print(Solution().mySqrt(8))
