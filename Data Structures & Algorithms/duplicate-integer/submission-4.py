class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        counts = {}
        for i in nums:
            if i not in counts:
                counts[i] = 1
            else:
                counts[i] += 1
        for i in counts:
            if counts[i] > 1:
                return True
        return False