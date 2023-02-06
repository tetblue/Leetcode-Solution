class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, area, min_height = 0, len(height) - 1, 0, 0
        while left < right:
            if height[left] > min_height and height[right] > min_height:
                min_height=min(height[left], height[right])
                area = max(area, (right - left) * min_height)
            if height[left] < height[right]:
                left+=1
                while height[left]<min_height:
                    left+=1
            else:
                right-=1
                while height[right]<min_height:
                    right-=1			
        return area
