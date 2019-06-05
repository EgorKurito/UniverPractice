import math

class Vec2D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, other):
        return Vec2D(self.x + other.x, self.y + other.y, self.z + other.z)

    def sub(self, other):
        return Vec2D(self.x - other.x, self.y - other.y, self.z - other.z)

    def mul(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def scMul(self, scalar):
        return Vec2D(scalar*self.x, scalar*self.y, scalar*self.z)

    def abs(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __str__(self):
        return '(%g, %g, %g)' % (self.x, self.y, self.z)

    def vecMul(self, other):
        return Vec2D(self.y*other.z - self.z*other.y, -1*(self.x*other.z - self.z*other.x), self.x*other.y - self.y*other.x)

a = Vec2D(1,14,1)
b = Vec2D(2,2,14)

c = a.scMul(4)

print(c)
