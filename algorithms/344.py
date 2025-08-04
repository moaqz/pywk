from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def invert(s: List[str], low: int, high: int):
            if low > high:
                return

            temp = s[low]
            s[low] = s[high]
            s[high] = temp

            low += 1
            high -= 1

            invert(s, low, high)

        invert(s, 0, len(s) - 1)
        print(s)


print(
    Solution().reverseString(["h", "e", "l", "l", "o"]),
    Solution().reverseString(["H", "a", "n", "n", "a", "h"]),
    sep="\n",
)
