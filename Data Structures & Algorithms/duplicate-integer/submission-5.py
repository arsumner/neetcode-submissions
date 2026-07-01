class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {i: 0 for i in nums}
        for i in nums:
            if counts[i] == 1:
                return True
            else:
                counts[i] += 1
        return False