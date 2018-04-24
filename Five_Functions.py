'''
You decide to test if your oddly-mathematical heating company is fulfilling its All-Time Max, Min, Mean and Mode Temperature Guarantee™.

Write a class TempTracker with these methods:

insert()—records a new temperature
get_max()—returns the highest temp we've seen so far
get_min()—returns the lowest temp we've seen so far
get_mean()—returns the mean ↴ of all temps we've seen so far
get_mode()—returns a mode ↴ of all temps we've seen so far
Optimize for space and time. Favor speeding up the getter methods get_max(), get_min(), get_mean(), and get_mode() over speeding up the insert() method.

get_mean() should return a float, but the rest of the getter methods can return integers. Temperatures will all be inserted as integers. We'll record our temperatures in Fahrenheit, so we can assume they'll all be in the range 0..1100..110.

If there is more than one mode, return any of the modes.

'''



def __init__(self):
    self.maxVal = float('-inf')
    self.minVal = float('inf')

    self.tempsRec = 0
    self.total = 0.0
    self.mean = None
    
    self.mode = 0
    self.maxOccur = 0
    self.repeatNum = [0] * 130
    
def insert(self, temperature):
    
    self.maxVal = max(self.maxVal, temperature)
    self.minVal = min(self.minVal, temperature)
    
    self.total += temperature
    self.tempsRec += 1
    self.mean = self.total/self.tempsRec
    
    self.repeatNum[temperature] += 1
    
    if self.repeatNum[temperature] > maxOccur:
        maxOccur = self.repeatNum[temperature]
        self.mode = temperature
    

def get_max(self):
    return self.maxVal
    
def get_min(self):
    return self.minVal
    
def get_mean(self):
    return self.mean

def get_mode(self):
    return self.mode, self.maxOccur

def my_function(arg):
    # write the body of your function here
    return 'running with %s' % arg

# run your function through some test cases here
# remember: debugging is half the battle!
print my_function('test input')
