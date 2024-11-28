class Solution:
    def myAtoi(self, s):
        # Code here
        s = s.lstrip()
        
        if not s: 
            return 0
        
        sign = 1
        index = 0
        
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        num = 0
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            num = num * 10 + digit
            index += 1
            
            
            if sign == 1 and num >= 2**31:
                return 2**31 - 1
            if sign == -1 and num > 2**31:
                return -2**31
        
        return sign * num
