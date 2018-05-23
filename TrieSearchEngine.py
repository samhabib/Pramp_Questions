'''
Input: root_dict - A root node for our trie dictionary that we will navigate to see if it has the next letter in the string to move forward and repeat
       site_string - The site string that we will be checking to see if it has been visited by the crawler
Output: True or False whether or not the site_string was already in the Trie
Axioms:
    1. Strings can be empty
    2. Assume string will be in ASCII
    3. Capitalization doesn't matter
    4. Remember to take into account that www. isn't mandatory to type before your text

Approach:
    1. In a different function, we worry about storing the values in the root dictionary so all we need to worry about here is finding if the string is in the trie
    2. We start with checking whether the first 4 chars of the site_string are www. or not. If they are we start the counter at 4, otherwise we start at 0
    3. Then we check comparing out string at the index to the trie to see if the current node's dictionary has a matching char.
    4. If there is not a match, we say it failed and then we make a request to add the remainder to the trie because the remainder of the string will now enter the visited group
    5. If it matches, we just increment the index and move into the matching node's dictionary
    6. Repeat until we reach the end of the site_string and then check and look for a special char that is not used in websites like *
    7. If * is found, return True otherwise return False
'''
def site_check(root_dict, site_string):
    
    if site_string is None:
        add_word(root_dict, site_string)
        return False
        
    if "www." in site_string[0:4]:
        increment = 4
    else:
        increment = 0

        
    curr_dict = root_dict
    site_string = site_string + '*'

    
    while(increment <= len(site_string)):
        
        if site_string[increment] in curr_dict:
            curr_dict = curr_dict[site_string[increment]]
            increment += 1
        else:
            add_word(curr_dict, site_string[increment:])
            return False
    
    return True

'''
Input: root_dict - Where we continue adding the remainder of the site_string that was not already in the trie
       site_string - The remainder of the string we have to add to the trie
Output: returns nothing, but will edit the root_dict to have a path so the crawler will know it visited the site_string in the past
Axioms:
    1. site_string will already have a * char at the end of it so no need to add it back to the string

Approach:
    1.Cycle through remaining char's and add them as new dict's within new dict's till you reach end of string
'''


def add_word(root_dict,site_string):
    
    for char in site_string:
        root_dict[char] = {}
        root_dict = root_dict[char]
        
