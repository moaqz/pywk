from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = ((high - low) // 2) + low

            if nums[mid] == mid:
                low = mid + 1
            else:
                high = mid - 1

        return low


print(
    Solution().missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]),
    Solution().missingNumber([3, 0, 1]),
    Solution().missingNumber([0, 1]),
    sep="\n"
)
