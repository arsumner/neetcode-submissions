class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapp = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in mapp:
                print([mapp[difference], i])
                return [mapp[difference], i]
            else:
                mapp[nums[i]] = mapp.get(i, i)