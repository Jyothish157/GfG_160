class Solution:
    # Function to find maximum product subarray
    def maxProduct(self, arr):
        if not arr:
            return 0
        
        max_ending_here = arr[0]
        min_ending_here = arr[0]
        max_so_far = arr[0]
        
        for i in range(1, len(arr)):
            num = arr[i]
            if num < 0:
                # Swap the max and min when a negative number is encountered
                max_ending_here, min_ending_here = min_ending_here, max_ending_here
            
            # Update max_ending_here and min_ending_here
            max_ending_here = max(num, max_ending_here * num)
            min_ending_here = min(num, min_ending_here * num)
            
            # Update the global maximum product
            max_so_far = max(max_so_far, max_ending_here)
        
        return max_so_far
