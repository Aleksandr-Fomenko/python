from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        nums1[m:] = nums2[:n]
        return nums1.sort()

if __name__ == '__main__':
    print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
    print(Solution().merge(nums1 = [1], m = 1, nums2 = [], n = 0))
    print(Solution().merge(nums1 = [0], m = 0, nums2 = [1], n = 1))

