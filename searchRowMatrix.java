class Solution {
    // Function to search a given number in row-column sorted matrix.
    public boolean searchRowMatrix(int[][] mat, int x) {
        // code here
        for(int[] row : mat){
            int index = Arrays.binarySearch(row,x);
            if(index>=0){
                return true;
            }
        }
        return false;
    }
}
