class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        counts = {}

        for i in nums:
            counts[i] = counts.get(i, 0) + 1

        for key in counts:
            if counts[key] != 1:
                return True

        return False

test = Solution()
test.hasDuplicate([1,2,3,3])

