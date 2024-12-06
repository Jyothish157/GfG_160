class Solution:

    def areRotations(self, s1: str, s2: str) -> bool:
        # Code here
        if len(s1) != len(s2):
            return False
        
        concatenated = s1 + s1
        
        return s2 in concatenated
