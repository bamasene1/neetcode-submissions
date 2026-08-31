class Solution:
    def trap(self, height: List[int]) -> int:
        lMax = 0
        rMax = 0
        water = 0

        left = 0
        right = len(height) - 1

        while left < right:
            if height[left] < height[right]:
                lMax = max(lMax,height[left])
                water += lMax - height[left]
                left +=1
            else:
                rMax = max(rMax, height[right])
                water += rMax - height[right]
                right -= 1
        
        return water