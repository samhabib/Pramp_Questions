'''

Array of Array Products
Given an array of integers arr, you’re asked to calculate for each index i the product of all integers except the integer at that index (i.e. except arr[i]). Implement a function arrayOfArrayProducts that takes an array of integers and returns an array of the products.

Solve without using division and analyze your solution’s time and space complexities.

Constraints:

[time limit] 5000ms

[input] array.integer arr

0 ≤ arr.length ≤ 20
[output] array.integer

'''


def array_of_array_products(arr):
  arrLen = len(arr)
  if (arrLen == 0) or (arrLen == 1):
    return []
  product = 1
  newArr = []
  for i in range(0,arrLen):
    newArr.insert(i, product)
    product *= arr[i]
  
  product = 1
  for i in range(arrLen-1,-1,-1):
    newArr[i]*=product
    product *= arr[i]
    
  return newArr
