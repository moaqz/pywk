class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


print(
    Solution().fib(2),
    Solution().fib(3),
    Solution().fib(4),
    sep="\n",
)
