def my_function(arg):
    x1 = arg[0][0]
    x2 = arg[1][0]
    y1 = arg[0][1]
    y2 = arg[1][1]
    w1 = arg[0][2]
    w2 = arg[1][2]
    h1 = arg[0][3]
    h2 = arg[1][3]
    
    xw = x_overlap(x1, x2, w1, w2)
    yh = y_overlap(y1, y2, h1, h2)
    if (xw[1] == 0) or(yh[1] == 0):
        print "No Overlap"
    else:
        print "left_x: " + str(xw[0])
        print "bottom_y: " + str(yh[0])
        print "width: " + str(xw[1])
        print "height: " + str(yh[1])

        
        

def x_overlap(x1, x2, w1, w2):
    if (x1+w1 > x2 >= x1):
        minW = min(x1+w1,x2+w2)
        
        return(x2, minW)
        
    elif(x2+w2 > x1 >= x2 ):
        minW = min(x1+w1,x2+w2)
        
        return(x1, minW)
    
    return (0,0)

def y_overlap(y1, y2, h1, h2):
    if (y1+h1 > y2 >= y1):
        minH = min(y1+h1,y2+h2)
        
        return(y2, minH)
        
    elif(y2+h2 > y1 >= y2 ):
        minH = min(y1+h1,y2+h2)
        
        return(y1, minH)
    
    return (0,0)
    
# run your function through some test cases here
# remember: debugging is half the battle!
print my_function(([1,1,1,1],[0,1,3,6]))
