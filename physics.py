import math


class Vector2:
    def __init__(self, x = 0, y = 0):

        self.x = x
        self.y = y
        self.mod = (x**2 + y**2)**(1/2)

    
    def __add__(self, other):

        result = Vector2(self.x + other.x, self.y + other.y)
        return(result)
    
    
    def __sub__(self, other):

        result = Vector2(self.x - other.x, self.y - other.y)
        return(result)
    
    
    def __mul__(self, other):

        if type(other) is Vector2:
            result = self.x * other.x + self.y + other.y
        
        else:
            result = Vector2(self.x * other, self.y * other)

        return(result)
    

    def __truediv__(self, other):

        result = Vector2(self.x / other, self.y / other)
        return(result)
    

    def unit(self):

        if self.mod != 0:
            result = self / self.mod

        else:
            result = Vector2(0, 1)

        return(result)
    
    def normal(self):

        result = Vector2(-self.y, self.x)
        return(result)
         


class MassPoint:

    def __init__(self, R = Vector2(0, 0), m = 1, g = 0):

        self.p = 0.1
        self.m = m
        self.r = ((self.m * 3) / (self.p * 4 * math.pi))**(1/3)
        if self.r >= 25:
            
            self.r = 25

        self.R = R
        self.V = Vector2(0, 0)
        self.A = Vector2(0, 0)
        self.F = Vector2(0, 0)
        self.nextF = Vector2(0, 0)
        self.g = g

    
    def SimulateStep(self, dt):

        self.AddForce(Vector2(0, -1) * self.g * self.m)
        
        self.F = self.nextF
        self.A = self.F / self.m
        self.V = self.V + self.A * dt
        self.R = self.R + self.V * dt

        self.nextF = Vector2(0, 0)


    def AddForce(self, F):

        self.nextF = self.nextF + F



class SpringJoint:

    def __init__(self, point1, point2, xn, k = 1):

        self.point1 = point1
        self.point2 = point2
        self.xn = xn
        self.k = k
        

    def CalculateForce(self):
        
        self.x = (self.point1.R - self.point2.R).mod
        self.Fmod = (self.x - self.xn) * self.k

        self.p1F = (self.point2.R - self.point1.R).unit() * self.Fmod
        self.p2F = (self.point1.R - self.point2.R).unit() * self.Fmod
        self.point1.AddForce(self.p1F)
        self.point2.AddForce(self.p2F)



class System:
    def __init__(self):

        self.MassPointDic = {}
        self.SpringJointDic = {}

    
    def AddMassPoint(self, name, R = Vector2(0, 0), m = 1, g = 0):

        self.MassPointDic[name] = MassPoint(R, m, g)
        

    def AddSpringJoint(self, name, point1, point2, xn, k = 1):

        self.SpringJointDic[name] = SpringJoint(self.MassPointDic[point1], self.MassPointDic[point2], xn, k)


    def SimulateStep(self, dt):

        for SJ in self.SpringJointDic.values():

            SJ.CalculateForce()


        for MP in self.MassPointDic.values():

            MP.SimulateStep(dt)


    def GetEnergy(self):

        Ek = 0
        Epe = 0

        for MP in self.MassPointDic.values():

            Ek = Ek + ((MP.V.mod)**2 * MP.m) / 2

        for SJ in self.SpringJointDic.values():

            
            x = (SJ.point1.R - SJ.point2.R).mod
            Epe = Epe + x**2 * 2
            
        




