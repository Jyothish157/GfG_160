class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals.sort(key=lambda x: x[1])
        
        count = 0
        last_end = float('-inf') 
        
        for start, end in intervals:
            if start < last_end:
                count += 1
            else:
                last_end = end
        
        return count
