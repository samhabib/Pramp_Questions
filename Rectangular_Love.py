import unittest


def find_rectangular_overlap(rect1, rect2):

    # Calculate the overlap between the two rectangles
    '''
    Input: 
    rect1 - Dictionary containing starting coordinates and width and height for rectangle 1
    rect2 - Dictionary containing starting coordinates and width and height for rectangle 2
    
    Output:
    intersect_rect - Dictionary containing starting coordinates and width and height for intersection rectangle
    
    Axioms:
    1. 3 Different situations to look out for
       - No intersection ---> return dict with 0 values
       - Normal intersection ---> find start of intersection and see what rect limits the height and what rect limits the width and return those valuse in a new dict
       - Intersection where one rect contains all of the other rect ---> return value of contained square
    2. Coordinates can be negative but height and width have to be greater than 0
    
    Approaches:
    1. Check to see if the range [left_x, left_x + width] for rect 1 has any matching values with the range
    [left_x, left_x + width] for rect 2
    
    2. If not return empty dict
    
    3. If so, set left_x for intersect_rect to max() of the two left_x and set width to min() of the two left_x + width of the respective rectangle

    4. Repeat steps 1 - 3 replacing left_x --> bottom_y and width --> height
    
    '''
    intersect_rect = {}
    intersect_rect['left_x'] = None
    intersect_rect['bottom_y'] = None
    intersect_rect['width'] = None
    intersect_rect['height'] = None
    
    if (rect1['left_x'] <=  rect2['left_x'] <  rect1['left_x'] +  rect1['width']) or (rect2['left_x'] <=  rect1['left_x'] <  rect2['left_x'] +  rect2['width']):
        
        if(rect1['bottom_y'] <=  rect2['bottom_y'] <  rect1['bottom_y'] +  rect1['height']) or (rect2['bottom_y'] <=  rect1['bottom_y'] <  rect2['bottom_y'] +  rect2['height']):
            intersect_rect['left_x'] = max(rect1['left_x'], rect2['left_x'])
            intersect_rect['bottom_y'] = max(rect1['bottom_y'], rect2['bottom_y'])
            
            new_width = min(rect1['left_x'] + rect1['width'], rect2['left_x'] + rect2['width'])
            new_width-= intersect_rect['left_x']
            
            new_height = min(rect1['bottom_y'] + rect1['height'], rect2['bottom_y'] + rect2['height'])
            new_height-= intersect_rect['bottom_y']
            
            intersect_rect['width'] = new_width
            intersect_rect['height'] = new_height
            
            return intersect_rect
        else:
            return intersect_rect
    else:
        return intersect_rect

# Tests

class Test(unittest.TestCase):

    def test_overlap_along_both_axes(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 3,
        }
        rect2 = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': 5,
            'bottom_y': 2,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


    def test_one_rectangle_inside_another(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 6,
            'height': 6,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_both_rectangles_the_same(self):
        rect1 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        expected = {
            'left_x': 2,
            'bottom_y': 2,
            'width': 4,
            'height': 4,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_horizontal_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 2,
            'bottom_y': 6,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_on_vertical_edge(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 2,
            'width': 3,
            'height': 4,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_touch_at_a_corner(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 3,
            'bottom_y': 3,
            'width': 2,
            'height': 2,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)

    def test_no_overlap(self):
        rect1 = {
            'left_x': 1,
            'bottom_y': 1,
            'width': 2,
            'height': 2,
        }
        rect2 = {
            'left_x': 4,
            'bottom_y': 6,
            'width': 3,
            'height': 6,
        }
        expected = {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None,
        }
        actual = find_rectangular_overlap(rect1, rect2)
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
