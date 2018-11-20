'''
 You are given a list of points on a coordinate plane. We need you find the convex hull formed by these points. The convex hull of a set X of points in the Euclidean plane is the smallest convex set that contains X. For instance: when X is a bounded subset of the plane, the convex hull may be visualized as the shape formed by a rubber band stretched around X. If a point lies on edge, it's included.

The points are presented as a list of coordinates [x, y] in which x and y are integers. The result returns as a sequence of indexes of points in the given list; points lie on the convex hull in clockwise order (see the picture). The sequence starts from the bottom leftmost point. Remember: You should return a list of indexes--not the points themselves.

Input: A list of coordinates. Each coordinate is a list of two integers.

Output: The list of indexes of coordinates from the given list.

Precondition:
2 < len(coordinates) < 10
all(0 < x < 10 and 0 < x < 10 for x, y in coordinates) 
'''



from math import acos, sqrt, pi
from operator import itemgetter
def checkio(data):
    def dist(a,b):
            # distance between points a and b
            return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
        
    def theta(pointA, pointB, pointC):
        # inner angle between vector BA et BC
        BA = (pointA[0]-pointB[0], pointA[1]-pointB[1])
        BC = (pointC[0]-pointB[0], pointC[1]-pointB[1])
        dot_prod = (BA[0]*BC[0]) + (BA[1]*BC[1])
        BA_length = sqrt((BA[0]**2 + BA[1]**2))
        BC_length = sqrt((BC[0]**2 + BC[1]**2))
        try:
            return round(acos(dot_prod / (BA_length * BC_length)), 10)
        except ZeroDivisionError: # vector dot product with vector of length = 0
            return 0
        except ValueError: # angle = Pi in certain cases of floating point arithmetic ...
            return pi

    hull = []
    starting_point = min(data)
    p = starting_point
    ending_point = None
    pointA = (p[0],p[1]+1) # first reference vector BA is parallel to the vertical
    pointB = p
    while starting_point != ending_point:
        hull.append(data.index(p))
        angle = pi
        k = []
        for point in data:
            if pointB != point  and theta(pointA, pointB, point) <= angle:
                angle = theta(pointA, pointB, point)
                p = point
                k.append((p,angle,dist(pointB,point)))
        # sort by angle and then by distance from ending_point, in cases of colinear points        
        if k :
            p = sorted(k, key = itemgetter(1,2))[0][0] 
        pointA = (p[0]+(p[0]-pointB[0]), p[1]+(p[1]-pointB[1])) 
        pointB = p
        ending_point = p
 
    return hull
            
    
    
    

if __name__ == '__main__':
    
    assert checkio([[7,4],[5,2],[4,7],[4,1],[3,6],[1,4]]) == [5,4,2,0,1,3]
    
    assert checkio(
        [[7, 6], [8, 4], [7, 2], [3, 2], [1, 6], [1, 8], [4, 9]]
    ) == [4, 5, 6, 0, 1, 2, 3], "First example"
    
    assert checkio(
        [[3, 8], [1, 6], [6, 2], [7, 6], [5, 5], [8, 4], [6, 8]]
    ) == [1, 0, 6, 3, 5, 2], "Second example"  
    assert checkio([[2,5],[5,5],[5,2],[2,2]]) == [3,0,1,2]

    assert checkio([[2,0],[1,1],[3,1],[2,2]]) == [1,3,2,0]
    print('pass for all tests')
