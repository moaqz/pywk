from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = low + ((high - low) // 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1

        return low


print(
    Solution().searchInsert([1, 3, 5, 6], 5),
    Solution().searchInsert([1, 3, 5, 6], 2),
    Solution().searchInsert([1, 3, 5, 6], 7),
    sep="\n",
)
