class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i,len(heights)):
                min_pol = min(heights[i],heights[j])
                max_area = max(max_area,min_pol * (j-i))
        return max_area