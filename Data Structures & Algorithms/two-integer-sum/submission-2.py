class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, val in enumerate(nums):
            difference = target - val
            if difference in seen:
                return [i, seen[difference]]
            seen[val] = i