'''
Time Planner
Implement a function meetingPlanner that given the availability, slotsA and slotsB, of two people and a meeting duration dur, returns the earliest time slot that works for both of them and is of duration dur. If there is no common time slot that satisfies the duration requirement, return null.

Time is given in a Unix format called Epoch, which is a nonnegative integer holding the number of seconds that have elapsed since 00:00:00 UTC, Thursday, 1 January 1970.

Each person’s availability is represented by an array of pairs. Each pair is an epoch array of size two. The first epoch in a pair represents the start time of a slot. The second epoch is the end time of that slot. The input variable dur is a positive integer that represents the duration of a meeting in seconds. The output is also a pair represented by an epoch array of size two.

In your implementation assume that the time slots in a person’s availability are disjointed, i.e, time slots in a person’s availability don’t overlap. Further assume that the slots are sorted by slots’ start time.

Implement an efficient solution and analyze its time and space complexities.

Constraints:

[time limit] 5000ms

[input] array.array.integer slotsA

1 ≤ slotsA.length ≤ 100
slotsA[i].length = 2
[input] array.array.integer slotsB

1 ≤ slotsB.length ≤ 100
slotsB[i].length = 2
[input] integer

[output] array.integer

'''

def meeting_planner(slotsA, slotsB, dur):
  aCount = 0
  bCount = 0
  
  while(aCount<len(slotsA) and bCount<len(slotsB)):
    minVal = max(slotsA[aCount][0], slotsB[bCount][0])
    maxVal = min(slotsA[aCount][1], slotsB[bCount][1])

    if minVal + dur <= maxVal:
      return[minVal, minVal+dur]
    
    elif slotsA[aCount][1] < slotsB[bCount][1]:
      aCount+=1
    else:
      bCount+=1
      
  return []
