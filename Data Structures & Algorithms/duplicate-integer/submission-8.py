class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        count = {} # hash map of value counts

        for i in range(len(nums)):
            
            count[nums[i]] = 1 + count.get(nums[i], 0)
            if count[nums[i]] > 1:
                return True
        return False
            


test = Solution()
test.hasDuplicate([1,2,3,3])

