#User function Template for python3

class Solution:
    def search(self, pat, txt):
        # code here
        indices = []
        pat_length = len(pat)
        txt_length = len(txt)

        for i in range(txt_length - pat_length + 1):
            if txt[i:i + pat_length] == pat:
                indices.append(i)

        return indices
