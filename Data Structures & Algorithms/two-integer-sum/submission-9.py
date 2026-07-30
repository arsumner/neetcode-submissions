class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            difference = target - n
            if difference in prevMap:
                return [prevMap[difference], i]
            prevMap[n] = i

        


test = Solution()
test.twoSum([5,5], 10)

