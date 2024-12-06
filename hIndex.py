class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        n = len(citations)
        count = [0] * (n + 1)
        
        for citation in citations:
            if citation >= n:
                count[n] += 1
            else:
                count[citation] += 1
        
        total = 0
        for h in range(n, -1, -1):
            total += count[h]
            if total >= h:
                return h
        
        return 0
