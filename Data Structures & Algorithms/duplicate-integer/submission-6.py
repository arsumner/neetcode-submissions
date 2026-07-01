class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        r = 1
        for i in range(len(nums) - 1):
            if nums[i] == nums[r]:
                return True
            else:
                r+=1
        return False