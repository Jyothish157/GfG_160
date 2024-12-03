class Solution:
    def minChar(self, s):
        #Write your code here
        def computeKMPTable(concat):
            n = len(concat)
            lps = [0] * n 
            length = 0 
            i = 1
            
            while i < n:
                if concat[i] == concat[length]:
                    length += 1
                    lps[i] = length
                    i += 1
                else:
                    if length != 0:
                        length = lps[length - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        rev_s = s[::-1]
        concat = s + "#" + rev_s
        lps = computeKMPTable(concat)
        longest_palindromic_suffix_length = lps[-1]
        min_chars_to_add = len(s) - longest_palindromic_suffix_length
        
        return min_chars_to_add
