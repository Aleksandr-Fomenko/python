from typing import List


def plusOne(digits: List[int]) -> List[int]:
    if len(digits) > 1:
        digitsData = int(''.join(map(str, digits)))
        digitsData += 1
        return [int(x) for x in str(digitsData)]
    else:
        digitsData = []
        t = str(digits[0] + 1)
        for i in t:
            digitsData.append(int(i))
        return digitsData


if __name__ == '__main__':
    print(plusOne([1, 2, 3]))
    print(plusOne([4, 3, 2, 1]))
    print(plusOne([9]))
