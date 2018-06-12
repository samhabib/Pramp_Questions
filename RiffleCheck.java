public class Solution {

    public static boolean riffleCheck(int[] half1, int[] half2, int[] shuffledDeck) {
        
        // write the body of your function here
        int ptr1 = 0;
        int ptr2 = 0;
        
        for(int x: shuffledDeck){
            
            if(ptr1 < half1.length && x == half1[ptr1]){
                ptr1++;
            } else if(ptr2 < half2.length && x == half2[ptr2]){
                ptr2++;
            } else{
                return false;
            }
        }
        return true;

    }

    public static void main(String[] args) {

        // run your function through some test cases here
        // remember: debugging is half the battle!
    }
}
