from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    numInd = {}
    for item in range(len(nums)):
        if target - nums[item] in numInd:
            return [nums.index(target - nums[item]), item]
        numInd[nums[item]] = item


if __name__ == '__main__':
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum([3, 2, 4], 6))
    print(twoSum([3, 3], 6))
