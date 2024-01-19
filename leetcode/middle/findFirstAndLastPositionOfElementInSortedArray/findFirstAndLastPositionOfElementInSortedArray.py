from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [i for i in range(len(nums)) if target == nums[i]]

        if len(nums) == 0 or len(res) == 0:
            return [-1, -1]
        else:
            return [res[0], res[-1]]


if __name__ == '__main__':
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 8))
    print(Solution().searchRange(nums = [5,7,7,8,8,10], target = 6))
    print(Solution().searchRange(nums = [], target = 0))
