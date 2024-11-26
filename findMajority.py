class Solution:

    def findMajority(self, arr):
        n = len(arr)
        if n == 0:
            return []

        
        count_map = {}
        for num in arr:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1

        
        threshold = n // 3

        
        result = []
        for candidate, count in count_map.items():
            if count > threshold:
                result.append(candidate)

        
        result.sort()
        
        return result
