import math
import numpy as np
from numpy.linalg import norm

class Point(object):

    COUNT = 0

    def __init__(self, x, y):
        '''Определим переменные x и y'''
        self.X = x
        self.Y = y

    def move(self, dx, dy):
        '''Определяет, куда движутся x и y'''
        self.X = self.X + dx
        self.Y = self.Y + dy

    def __str__(self):
        return "Point(%s,%s)"%(self.X, self.Y)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        return math.hypot(dx, dy)

    def distanceToLine(self, first, second):
        p = np.asarray((self.X, self.Y))
        p1 = np.asarray((first.X, first.Y))
        p2 = np.asarray((self.X, self.Y))
        return np.cross(p2-p1,p-p1)/np.linalg.norm(p2-p1)



def testPoint(x=0, y=0):
    p1 = Point(1,1)
    #print(p1)
    p2 = Point(3,3)
    #print(p2)

    p3 = Point(10,10)
    #print(p1.distance(p2))

    #print(p2.distance(p1))

    print(p1.distanceToLine(p2,p3))


def test(x=0, y=0):
    p = Point(x,y)

    print(type(p.getX))

#print(testPoint())
print(test())
