import collections
from collections import namedtuple

point = namedtuple("Point",{"x": 0,"y": 0 , "z" : 0})
newP = point(3,4,5)
print(newP.z)