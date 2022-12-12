class Solution { //bottom-up approach
    int nn;
    int[] s = new int[48];
    public int climbStairs(int n) {
        nn = n;
        return fun(0);
    }
    public int fun(int i) {
        if(i == nn) {
            return 1;
        }

        if(i+1 <= nn && s[i+1] == 0) {
            s[i+1] = fun(i+1);
        } 
        if(i+2 <= nn && s[i+2] == 0) {
            s[i+2] = fun(i+2);
        }
        return s[i+1]+s[i+2];
    }
}