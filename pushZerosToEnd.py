class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	for j in range(len(arr)):
    	    if arr[j] == 0:
    	        break
    	    
    	    
    	i = j - 1
    	
    	while j < len(arr) and i < j:
    	    
    	    if arr[j] == 0:
    	        j += 1
    	    else:
    	        arr[i+1],arr[j] = arr[j],arr[i+1]
    	        i += 1
