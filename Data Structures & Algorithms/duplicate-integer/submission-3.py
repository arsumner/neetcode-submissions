class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {i: 0 for i in nums}
        for i in nums:
            counts[i] += 1
        for i in counts:
            if counts[i] > 1:
                return True
        return False