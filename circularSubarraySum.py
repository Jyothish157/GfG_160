#User function Template for python3

#Complete this function
#Function to find maximum circular subarray sum.
def circularSubarraySum(arr):
    ##Your code here
    def kadane_max(arr):
        max_ending_here = max_so_far = arr[0]
        for x in arr[1:]:
            max_ending_here = max(x, max_ending_here + x)
            max_so_far = max(max_so_far, max_ending_here)
        return max_so_far

    
    def kadane_min(arr):
        min_ending_here = min_so_far = arr[0]
        for x in arr[1:]:
            min_ending_here = min(x, min_ending_here + x)
            min_so_far = min(min_so_far, min_ending_here)
        return min_so_far

    total_sum = sum(arr)
    max_normal = kadane_max(arr)
    min_normal = kadane_min(arr)


    if total_sum == min_normal:
        return max_normal

    return max(max_normal, total_sum - min_normal)
