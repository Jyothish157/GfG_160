class Solution:
    def kthMissing(self, arr, k):
        # code here
        missing_count = 0 
        current_number = 1 
        index = 0  
        
        while True:
            if index < len(arr) and arr[index] == current_number:
                index += 1
            else:
                missing_count += 1
        
            if missing_count == k:
                return current_number
            
            current_number += 1
