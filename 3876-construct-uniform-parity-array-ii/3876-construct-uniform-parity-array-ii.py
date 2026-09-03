class Solution:
    def uniformArray(self, nums):
        mini = min(nums)

        if mini % 2 == 1:
            return True

        for x in nums:
            if x % 2 == 1:
                return False

        return True 