from collections import Counter
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        test = []
        hh = Counter(nums)
        for i in set(nums):
            test.extend([i] * hh[i])

        for i in range(len(test)):
            nums[i] = test[i]

        return nums


if __name__ == '__main__':
    print(Solution().sortColors(nums = [2,0,2,1,1,0]))
    print(Solution().sortColors(nums = [2,0,1]))
