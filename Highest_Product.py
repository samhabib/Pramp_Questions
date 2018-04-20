def highest_product_of_3(list_of_ints):

    # Calculate the highest product of 3 integers
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items in list, cannot solve')
        
    
    high1 = max(list_of_ints[0],list_of_ints[1])
    low1 = min(list_of_ints[0],list_of_ints[1])
    high2 = list_of_ints[0] * list_of_ints[1]
    low2 = list_of_ints[0] * list_of_ints[1]
    high3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]
    
    for x in range(2, len(list_of_ints)):
        
        value = list_of_ints[x]
        
        high3 = max(high3, high2 * value, low2 * value)
        high2 = max(high2, high1 * value, low1 * value)
        low2 = min(low2, high1 * value, low1 * value)
        high1 = max(high1, value)
        low1 = min(low1, value)
        
    return high3

list_of_ints = [1, 10, -5, 1, -100]
print highest_product_of_3(list_of_ints)
