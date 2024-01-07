class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return True if n in [2**i for i in range(0,31)] else False


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(n = 1))
    print(Solution().isPowerOfTwo(n = 16))
    print(Solution().isPowerOfTwo(n = 3))
