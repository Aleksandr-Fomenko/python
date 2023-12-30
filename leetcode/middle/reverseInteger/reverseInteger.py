class Solution:
    def reverse(self, x: int) -> int:

        if x < 0:
            x *= -1
            x = int(str(x)[::-1]) * -1
        else:
            x = int(str(x)[::-1])

        return x if -2 ** 31 <= x <= 2 ** 31 - 1 else 0


if __name__ == '__main__':
    print(Solution().reverse(123))
    print(Solution().reverse(-123))
    print(Solution().reverse(120))
