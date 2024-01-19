from typing import List


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        mini, res = abs(arr[1] - arr[0]), [arr[0:2]]

        for i in range(2, len(arr)):
            diff = abs(arr[i] - arr[i - 1])

            if diff > mini:
                continue

            if diff < mini:
                mini, res = diff, list()

            res.append([arr[i - 1], arr[i]])

        return res

if __name__ == '__main__':
    print(Solution().minimumAbsDifference(arr = [4,2,1,3]))
    print(Solution().minimumAbsDifference(arr = [1,3,6,10,15]))
    print(Solution().minimumAbsDifference(arr = [3,8,-10,23,19,-4,-14,27]))

