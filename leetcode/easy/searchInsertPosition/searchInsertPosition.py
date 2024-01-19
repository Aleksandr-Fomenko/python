from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        for i in range(len(nums)):
            if target <= nums[i]:
                return i
            elif nums[i] == nums[-1]:
                return i + 1

if __name__ == '__main__':
    print(Solution().searchInsert(nums = [1,3,5,6], target = 5))
    print(Solution().searchInsert(nums = [1,3,5,6], target = 2))
    print(Solution().searchInsert(nums = [1,3,5,6], target = 7))
