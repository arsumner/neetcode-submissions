class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for i in nums:
            if nums[i] not in counts:
                count[i] = 1
            else:
                count[i] += 1
        for i in counts:
            if counts[i] > 1:
                return False
            else:
                return True