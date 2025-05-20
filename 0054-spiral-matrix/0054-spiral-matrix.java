class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int rows=matrix.length;
        int cols= matrix[0].length;
        int total = rows * cols;
        int[] result = new int[total];
        int top=0;
        int bottom =rows-1;
        int left=0;
        int right=cols-1;
        int i=0;
        while (i<total){
            for (int col=left; col<right+1;col++){
                if (i<total){
                    result[i]=matrix[top][col];
                    i+=1;
                }
                    
            }
            top+=1;
            for (int row=top; row<bottom+1;row++){
                if (i<total){
                    result[i]=matrix[row][right];
                    i+=1;
                }
                    
            }
            right-=1;

            for (int col=right; col>=left;col--){
                if (i<total){
                    result[i]=matrix[bottom][col];
                    i+=1;
                }
                    
            }
            bottom-=1;
            for (int row=bottom; row>=top;row--){
                if (i<total){
                    result[i]=matrix[row][left];
                    i+=1;
                }
                    
            }
            left+=1;


        }
        List<Integer> list = new ArrayList<>();
        for (int val : result) {
            list.add(val);
        }
        return list;

        
        
    }
}