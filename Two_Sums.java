class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
        Original Question:
        Given an array of integers, return indices of the two numbers such that they add up to a specific target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.
        */
    
    
    
        /*
        Input:
            - nums, an integer array containing all unique integers that we can use to add up to solve for target
            - target, an integer that we are trying to solve for by adding two numbers from the nums array together
        Output:
            - answer, an integer array with the two indices from nums that as values add up to target value
        Axioms:
            - target is assumed positive integer
            - nums may not be sorted
            - nums can be any size
            - nums can hold negative number
            - nums holds no duplicates
        Approach:
            - Greedy Algorithm
            - We cycle through nums once and for every value we run into, we check if its target counterpart is a key in our hashmap
            - If we find have already stored the key already we return the two values
            - If we did not already store its matching counterpart than we add the current value to the hashmap with its index as its value
            - If we cycle through the list and do not get a match than we return an empty array or false depending
            
        Run Time: O(N)
        Space Complexity: O(N)
        */
        HashMap<Integer,Integer> foundNumbers = new HashMap<Integer,Integer>();
        int[] arr = new int[2];
        if (nums.length < 2){
            return arr;
        }
        for(int x = 0; x < nums.length; x++){
            
            if (foundNumbers.get(target - nums[x]) == null){
                foundNumbers.put(nums[x], x );
                
            }else{
                arr[0] = foundNumbers.get(target - nums[x]);
                arr[1] = x;
                return arr;
            }
            
        }
        return arr;
    }
    
}
