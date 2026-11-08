class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        amount = -1
        while l < r:
            # print(f"r: {r}, l: {l}, heights[l]: {heights[l]}, heights[r]: {heights[r]}, amount: {amount}")
            temp_amount = (r-l) * min(heights[l], heights[r])
            amount = max(temp_amount, amount)
            if heights[l] > heights[r]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return amount
