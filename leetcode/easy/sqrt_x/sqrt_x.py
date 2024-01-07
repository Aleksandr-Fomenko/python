from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        return sorted(nums1[0:m] + nums2[0:n])


if __name__ == '__main__':
    print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3))
    print(Solution().merge(nums1 = [0], m = 0, nums2 = [1], n = 1))
    print(Solution().merge(nums1 = [1], m = 1, nums2 = [], n = 0))
