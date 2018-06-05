import java.io.*;
import java.util.*;



/*
he Westfield Mall management is trying to figure out what the busiest moment at the mall was last year. You’re given data extracted 
from the mall’s door detectors. Each data point is represented as an integer array whose size is 3. The values at indices 0, 1 and 2 
are the timestamp, the count of visitors, and whether the visitors entered or exited the mall (0 for exit and 1 for entrance), 
respectively. Here’s an example of a data point: [ 1440084737, 4, 0 ].

Note that time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed 
since 00:00:00 UTC, Thursday, 1 January 1970.

Given an array, data, of data points, write a function findBusiestPeriod that returns the time at which the mall reached its busiest 
moment last year. The return value is the timestamp, e.g. 1480640292. Note that if there is more than one period with the same visitor 
peak, return the earliest one.

Assume that the array data is sorted in an ascending order by the timestamp. Explain your solution and analyze its time and space 
complexities.
*/



class Solution {
	
  static int findBusiestPeriod(int[][] data) {
    // your code goes here
    /*
    Input: data, 2 Dimensional int Array
    Output: int timestamp of busiest time of the mall
    Axioms:
    -Array is sorted by timestamp in ascending order
    -Assume only valid inputs. No negatives
    -[0][0] index is for timestamp
    -[0][1] index is for number of people entering/leaving
    -[0][2] index is 0 for leaving and 1 for entering
    -There can be repeat timestamp entries
    Approach:
      1. We increment through the timestamps with a for loop in ascending order
      2. We start keeping track of the first timestamp and add or subtract as many people enter or leave into a total value called currCust
      3. Once we reach a new timestamp, before we add or subtract the customers, we check if currCust is bigger than our maxCust value if so we set it equal to maxCust and set the int busPeriod to that time stamp value.
      4. Once we finish the list we check the final values in our currCust and see if its greater, if so then we set that equal to our maxCust and busPeriod otherwise we return our current busPeriod
    */
    int busPeriod = data[0][0], maxCust = 0, currCust = 0, currTime = data[0][0]; 

    for(int x = 0; x < data.length; x++){
      
      if (data[x][0] != currTime){
        
        if (currCust > maxCust){
          maxCust = currCust;
          busPeriod = currTime;
        }
        currTime = data[x][0];
        
      }
      
      if (data[x][2] == 1){
        currCust+=data[x][1];
      }else{
        currCust-=data[x][1];
      }
      
    }
    if (currCust > maxCust){
      busPeriod = currTime;
    }
    return busPeriod;
  }

  public static void main(String[] args) {
    
  }

}
