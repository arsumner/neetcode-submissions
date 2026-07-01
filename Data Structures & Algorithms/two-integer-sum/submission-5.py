class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapp = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in mapp:
                print([mapp[difference], i])
                return [i, mapp[difference]]
            else:
                mapp[nums[i]] = i