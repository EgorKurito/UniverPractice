import math
import numpy as np
from numpy.linalg import norm
from sympy import *
from sympy.abc import x, y, z

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
        print(other.X, type(other.X))
        print(' ')
        print(other.Y, type(other.Y))
        print(' ')
        print(other.Z, type(other.Z))
        #return type(other.X)

        dx = self.X - other.X
        dy = self.Y - other.Y
        dz = self.Z - other.Z
        return math.sqrt(dx**2 + dy**2 + dz**2)

    def distanceToLine(self, a,b,c,q,p,t):

        def strToInt(n):
            for a in list(n):
                if a == '/':
                    index = list(n).index('/')
                    s = int(n[:index])/int(n[index+1:])
                    return float("%.2f" % s)
            return float(n)

        m0 = (x-self.X)*q + (y-self.Y)*p + (z-self.Z)*t
        print('m0', m0)
        m1 = (x+a)/q - (y+b)/(p)
        print('m1', m1)
        m2 = (x+a)/q - (z+c)/t
        print('m2', m2)
        m3 = (z+c)/t - (y+b)/(p)
        print('m3', m3)

        solve = (str(linsolve([m1,m2,m3,m0],(x,y,z)))[2:-2]).split(',')
        print('solve:', solve)
        print('type solve:', type(solve))

        H = Point(strToInt(str(solve[0])),strToInt(str(solve[1])),strToInt(str(solve[2])))
        print('H:',H)
        print('type H:', H)
        return self.distance(H)




def testPoint(x=0, y=0):
    p1 = Point(2,-4,-1)
    #print(p1)
    p2 = Point(1,2,3)
    #print(p2)

    p3 = Point(1,1,1)
    #print(p1.distance(p2))

    #print(p2.distance(p1))
    #print(p1.distanceToLine(1,0,5,2,-1,5))
    #print(p2.distanceToLine(1,0,5,2,-1,5))
    #print(p3.distanceToLine(1,0,5,2,-1,5))
    #print(p1.triangleSquare(p2,p3))



def strToInt(n):
    for a in list(n):
        print('a:', a)
        if a == '/':
            index = list(n).index('/')
            s = int(n[:index])/int(n[index+1:])
            return float("%.2f" % s)
    return float(n)
print(strToInt('1/15'))
print(type(strToInt('1/15')))
