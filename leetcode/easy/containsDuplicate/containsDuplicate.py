from typing import List


def containsDuplicate(nums: List[int]) -> bool:
    return False if len(nums) == len(list(dict.fromkeys(nums))) else True


if __name__ == '__main__':
    print(containsDuplicate([1, 2, 3, 1]))
    print(containsDuplicate([1, 2, 3, 4]))
    print(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
