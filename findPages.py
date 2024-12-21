def findPages(self, arr, k):
        #code here
        n = len(arr)
        
        if k > n:
            return -1
        
        low = max(arr)  
        high = sum(arr)  
        
        def canAllocate(maxPages):
            student_count = 1
            current_sum = 0
            
            for pages in arr:
                current_sum += pages
                if current_sum > maxPages:
                    student_count += 1
                    current_sum = pages  
                    if student_count > k:  
                        return False
            
            return True
        
        result = high  
        
        while low <= high:
            mid = (low + high) // 2
            
            if canAllocate(mid):
                result = mid  
                high = mid - 1
            else:
                low = mid + 1  
        
        return result
