class Solution {
    public int climbStairs(int n) {
         int[] memo = new int[n+1];
        return fibHelper(n,memo);
        
    }

    private int fibHelper(int n, int[] memo){
        if(n<=2){
            return n;
        }

        if(memo[n] != 0){
            return memo[n];
        }

        memo[n] = fibHelper(n-1,memo)+ fibHelper(n-2,memo);
        return memo[n];

        
    }
}