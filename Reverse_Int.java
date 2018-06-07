class Solution {
    
    
    public int reverse(int x) {
        if((x > Math.pow(2,31)-1)||(x < Math.pow(-2,31))){
            return 0;
        }
        int negative = 1;
        if(x<0){
            negative = -1;
            x*=-1;
        }
        String ans ="";
        String convertedInt = Integer.toString(x);
        
        for(int y = convertedInt.length() - 1; y > -1; y--){
            ans += String.valueOf(convertedInt.charAt(y));
        }
        
        try {
            return Integer.parseInt(ans) * negative;
        }catch (NumberFormatException e) {
            return 0;
        }
    }
}
