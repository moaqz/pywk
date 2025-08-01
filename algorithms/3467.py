from typing import List


class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        for idx in range(len(nums)):
            if nums[idx] % 2 == 0:
                nums[idx] = 0
            else:
                nums[idx] = 1

        def sort(arr: List[int]) -> List[int]:
            for i in range(1, len(arr)):
                temp = arr[i]
                j = i - 1

                while j >= 0 and temp < arr[j]:
                    arr[j + 1] = arr[j]
                    j -= 1

                arr[j + 1] = temp

            return arr

        return sort(nums)


print(
    Solution().transformArray([4,3,2,1]),
    Solution().transformArray([1, 5, 1, 4, 2]),
    sep="\n",
)
