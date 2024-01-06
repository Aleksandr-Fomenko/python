class Solution:
    def romanToInt(self, s: str) -> int:
        dictSymbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0

        for index in range(len(s)):
            if index < len(s) - 1 and dictSymbol[s[index]] < dictSymbol[s[index + 1]]:
                result -= dictSymbol[s[index]]
            else:
                result += dictSymbol[s[index]]

        return result

if __name__ == '__main__':
    print(Solution().romanToInt("III"))
    print(Solution().romanToInt("LVIII"))
    print(Solution().romanToInt("MCMXCIV"))