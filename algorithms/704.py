from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = high // 2

        while low <= high:
            val = nums[mid]

            if val == target:
                return mid
            elif val < target:
                low = mid + 1
            elif val > target:
                high = mid - 1

            mid = low + (abs(low - high) // 2)

        return -1


print(
    Solution().search([-1, 0, 3, 5, 9, 12], 9),
    Solution().search([-1, 0, 3, 5, 9, 12], 2),
    sep="\n",
)
