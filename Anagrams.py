class Solution:
    def areAnagrams(self, s1, s2):
        #code here
        if len(s1) != len(s2):
            return False
        
        char_count = {}
        
        for char in s1:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        for char in s2:
            if char in char_count:
                char_count[char] -= 1
            else:
                return False
        
        for count in char_count.values():
            if count != 0:
                return False
        
        return True
