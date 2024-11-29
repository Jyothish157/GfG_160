class Solution:
    def addBinary(self, s1: str, s2: str) -> str:
    
        s1 = s1.lstrip('0')
        s2 = s2.lstrip('0')
        
        
        if not s1 and not s2:
            return "0"
        
    
        result = []
        carry = 0
        

        if len(s1) < len(s2):
            s1, s2 = s2, s1
        
        i, j = len(s1) - 1, len(s2) - 1
        
        while i >= 0 or j >= 0 or carry:
            bit1 = int(s1[i]) if i >= 0 else 0
            bit2 = int(s2[j]) if j >= 0 else 0
            
            total = bit1 + bit2 + carry
            result.append(str(total % 2))
            carry = total // 2
            
            i -= 1
            j -= 1
        
        result.reverse()
        
        return ''.join(result)
