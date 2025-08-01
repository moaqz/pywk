from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            temp = nums[i]
            temp_idx = None
            has_shift_elements = False

            for j in range(i - 1, -1, -1):
                if temp < nums[j]:
                    nums[j + 1] = nums[j]
                    has_shift_elements = True
                else:
                    if has_shift_elements:
                        temp_idx = j + 1

                    break

            if has_shift_elements:
                if temp_idx is not None:
                    nums[temp_idx] = temp
                else:
                    # edge case where the value is less than all.
                    nums[0] = temp

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False


print(
    Solution().containsDuplicate([1, 3, 2, 1]),
    Solution().containsDuplicate([1, 2, 3, 4]),
    Solution().containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]),
    Solution().containsDuplicate([1, 2, 3, 0]),
    sep="\n",
)
