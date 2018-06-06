class Solution {
    
    /*
    
    Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

    P   A   H   N
    A P L S I I G
    Y   I   R


    Example 2:

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I
    
    
    Input:
        - String s, pre converted string
        - int numRows, number of rows in zigzag requirement
    Output:
        - String ans, converted string to read in zig zag motion
    Axioms:
        - String can be empty
        - String can be length 1
        - numRows can be 0
        - numRows can be 1
        - Case-sensitive
    Approach:
        - Most important thing is to recognize the pattern of how the zig zag works because it is very consistent
        - For the first and last row, it is always reading from a consistent difference of indices away from each other
        - For every other row, it is constantly switching from two different numbers to increment to the next char
        - Ex. In Example 2, first row is spaced consistently by +6 indices
        - But for the second row, it constantly switches beteween +4 and +2 indices
        - The rows constant switches will always add up to our first rows index switch so we have to make sure to keep track of that.
    Runtime: O(n)
    SpaceComplexity: O(1)
    
    */
    public String convert(String s, int numRows) {
        
        if(numRows <= 1){
            return s;
        }
        int buffCol = numRows / 2;;
        String ans = "";
        int firstInc = (numRows-1)*2;
        for(int x = 0; x < numRows; x++){
            int count = x;
            int switchVal =(x*2);

            if(x == 0 || x == numRows-1){
                for(int y = x; y < s.length(); y+=firstInc){
                    ans += String.valueOf(s.charAt(y));
                }
            }else{
                for(int y = x; y < s.length(); y+=switchVal){
                    ans += String.valueOf(s.charAt(y));
                    switchVal = firstInc - switchVal;
                }
            }
        }
        return ans;
    }
}
