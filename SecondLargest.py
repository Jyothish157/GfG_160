class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        lar = -1
        sec_lar = -1
        
        for num in arr:
            if num > lar:
                sec_lar = lar
                lar = num
            elif num > sec_lar and num < lar:
                sec_lar = num
        
        return sec_lar if sec_lar != -1 else -1
