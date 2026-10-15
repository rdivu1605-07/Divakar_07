class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            seen = [False] * 101
            distinct = 0

            for j in range(i, n):
                num = nums[j]

                if not seen[num]:
                    seen[num] = True
                    distinct += 1

                ans += distinct * distinct

        return ans 