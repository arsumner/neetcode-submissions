class Solution:
    def maxArea(self, heights: List[int]) -> int:

        result = 0
        l, r = 0, len(heights) - 1

        while l < r:
            dist = r - l
            height = min(heights[l], heights[r])
            area = dist * height
            result = max(area, result)

            if heights[l+1] >= heights[r-1]:
                l += 1
            else:
                r -= 1
                
        return result
