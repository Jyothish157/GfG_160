class Solution {
    int getMinDiff(int[] arr, int k) {
        Arrays.sort(arr);
        
        int diff = arr[arr.length - 1] - arr[0];
        int min = arr[0] + k;
        int max = arr[arr.length - 1] - k;
        
        for(int i = 0; i < arr.length - 1; i++){
            int curmax = Math.max(max, arr[i]+k); 
            int curmin = Math.min(min, arr[i + 1] - k);
            
            if(curmin < 0) continue;
            
            diff = Math.min(diff,curmax - curmin);
        }        
        
        return diff;
    }
}
