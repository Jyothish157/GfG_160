class Solution:
    
    def searchMatrix(self, mat, x): 
    	# code here 
    	if not mat or not mat[0]:
            return False
        
        n = len(mat)     
        m = len(mat[0])   
        
        row, col = 0, m - 1
        
        while row < n and col >= 0:
            if mat[row][col] == x:
                return True
            elif mat[row][col] > x:
                col -= 1 
            else:
                row += 1 
        
        return False
