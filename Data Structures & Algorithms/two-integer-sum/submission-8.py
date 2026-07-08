class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hash = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hash:
                return [hash[diff], i]
            hash[n] = i



test = Solution()
test.twoSum([5,5], 10)

