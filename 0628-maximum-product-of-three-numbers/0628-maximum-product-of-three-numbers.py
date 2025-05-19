class Solution(object):
    def maximumProduct(self, nums):
        max1 = max2 = max3 = float('-inf')
        min1 = min2 = float('inf')
        
        for n in nums:
            # Update max values
            if n > max1:
                max3 = max2
                max2 = max1
                max1 = n
            elif n > max2:
                max3 = max2
                max2 = n
            elif n > max3:
                max3 = n
            
            # Update min values
            if n < min1:
                min2 = min1
                min1 = n
            elif n < min2:
                min2 = n
        
        return max(max1 * max2 * max3, max1 * min1 * min2)
