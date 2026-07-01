class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        l, r = 0, len(numbers) - 1

        while l < r:

            if (numbers[l] + numbers[r]) == target:
                return [l + 1, r + 1]
            else:
                if (numbers[l] + numbers[r]) <= target:
                    l += 1
                else:
                    r -= 1
        return []


test = Solution()
test.twoSum([1,2,3,4,5,6], 10)