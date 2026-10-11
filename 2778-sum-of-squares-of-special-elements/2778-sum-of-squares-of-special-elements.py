from typing import List

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                result += nums[i - 1] ** 2

                j = n // i
                if i != j:
                    result += nums[j - 1] ** 2

        return result 