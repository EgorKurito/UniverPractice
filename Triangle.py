import math
import numpy as np
from numpy.linalg import norm

class Point(object):

    COUNT = 0

    def __init__(self, x, y, z):
        '''Определим переменные x и y и z'''
        self.X = x
        self.Y = y
        self.Z = z

    def move(self, dx, dy, dz):
        '''Определяет, куда движутся x и y'''
        self.X = self.X + dx
        self.Y = self.Y + dy
        self.Z = self.Z + dz

    def __str__(self):
        return "Point(%s,%s,%s)"%(self.X, self.Y, self.Z)

    def getX(self):
        return self.X

    def getY(self):
        return self.Y

    def getZ(self):
        return self.Z

    def distance(self, other):
        dx = self.X - other.X
        dy = self.Y - other.Y
        dz = self.Z - other.Z
        return math.sqrt(dx**2 + dy**2 + dz**2)

    def distanceToLine(self, first, second):
        pass


def testPoint(x=0, y=0):
    p1 = Point(1,1,1)
    #print(p1)
    p2 = Point(3,3,3)
    #print(p2)

    p3 = Point(10,10,10)
    #print(p1.distance(p2))

    #print(p2.distance(p1))

    print(p1.triangleSquare(p2,p3))


def test(x=0, y=0):
    p = Point(x,y)

    print(type(p.getX))

#print(testPoint())
print(testPoint())
